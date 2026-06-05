import React, { useMemo, useState } from 'react';
import {
  AlertTriangle,
  CheckCircle2,
  CircleDashed,
  Clock3,
  Cpu,
  Download,
  FileArchive,
  Loader2,
  RefreshCw,
  Server,
  ShieldCheck,
  Terminal,
  XCircle,
} from 'lucide-react';

const PIPELINE = [
  'Intent Extraction',
  'Planning',
  'IR Generation',
  'Validation',
  'Repair',
  'Runtime Launch',
  'Health Check',
  'Export',
];

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function stageTone(status) {
  if (status === 'completed') return 'border-emerald-300 bg-emerald-50 text-emerald-800';
  if (status === 'running') return 'border-sky-300 bg-sky-50 text-sky-800';
  if (status === 'failed' || status === 'blocked') return 'border-rose-300 bg-rose-50 text-rose-800';
  if (status === 'skipped') return 'border-amber-300 bg-amber-50 text-amber-800';
  return 'border-zinc-200 bg-white text-zinc-500';
}

function statusIcon(status, isCompiling) {
  if (status === 'completed') return <CheckCircle2 className="h-4 w-4" />;
  if (status === 'failed' || status === 'blocked') return <XCircle className="h-4 w-4" />;
  if (status === 'skipped') return <Clock3 className="h-4 w-4" />;
  if (status === 'running' || isCompiling) return <Loader2 className="h-4 w-4 animate-spin" />;
  return <CircleDashed className="h-4 w-4" />;
}

function formatSeconds(value) {
  if (typeof value !== 'number') return '0.0s';
  return `${value.toFixed(1)}s`;
}

function App() {
  const [prompt, setPrompt] = useState('');
  const [isCompiling, setIsCompiling] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const stageMap = useMemo(() => {
    const map = new Map();
    (result?.stages || []).forEach((stage) => map.set(stage.stage, stage));
    return map;
  }, [result]);

  const providerMetrics = result?.provider_metrics || {};
  const metrics = result?.metrics || {};
  const fallbackEvents = providerMetrics.fallback_events || [];
  const repairTrace = result?.repair_trace || [];
  const healthChecks = result?.runtime?.health_report?.checks || [];
  const exportReady = Boolean(result?.download_url);
  const currentStage = isCompiling
    ? 'Backend pipeline running'
    : [...stageMap.values()].at(-1)?.stage || 'Idle';

  const handleCompile = async () => {
    if (!prompt.trim()) return;

    setIsCompiling(true);
    setResult(null);
    setError(null);

    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 300000);
      const res = await fetch(`${API_BASE}/compile`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
        signal: controller.signal,
      });
      clearTimeout(timeoutId);

      const data = await res.json();
      if (!res.ok) {
        const errMsg = data?.detail?.message || data?.detail || data?.message || 'Compilation failed';
        throw new Error(typeof errMsg === 'string' ? errMsg : JSON.stringify(errMsg));
      }
      setResult(data);
    } catch (err) {
      if (err.name === 'AbortError') {
        setError('Compilation timed out after 5 minutes.');
      } else if (err.message === 'Failed to fetch' || err.message?.includes('NetworkError')) {
        setError('Backend is not reachable at http://localhost:8000.');
      } else {
        setError(err.message);
      }
    } finally {
      setIsCompiling(false);
    }
  };

  return (
    <main className="min-h-screen bg-zinc-100 text-zinc-950">
      <div className="mx-auto flex max-w-7xl flex-col gap-5 px-4 py-5 lg:px-6">
        <header className="flex flex-col gap-3 border-b border-zinc-200 pb-4 md:flex-row md:items-end md:justify-between">
          <div>
            <div className="mb-2 flex items-center gap-2 text-sm font-semibold text-zinc-600">
              <Cpu className="h-4 w-4 text-sky-700" />
              AI App Compiler
            </div>
            <h1 className="text-3xl font-semibold tracking-normal text-zinc-950">Compiler Console</h1>
          </div>
          <div className="flex items-center gap-2 rounded-lg border border-zinc-200 bg-white px-3 py-2 text-sm text-zinc-700">
            {isCompiling ? <Loader2 className="h-4 w-4 animate-spin text-sky-700" /> : <Terminal className="h-4 w-4 text-zinc-500" />}
            <span>{currentStage}</span>
          </div>
        </header>

        <section className="grid gap-5 lg:grid-cols-[420px_1fr]">
          <div className="space-y-5">
            <div className="rounded-lg border border-zinc-200 bg-white p-4 shadow-sm">
              <label className="mb-2 block text-sm font-medium text-zinc-700" htmlFor="prompt">
                Prompt
              </label>
              <textarea
                id="prompt"
                className="min-h-44 w-full resize-none rounded-lg border border-zinc-300 bg-white px-3 py-3 text-sm leading-6 text-zinc-950 outline-none transition focus:border-sky-600 focus:ring-2 focus:ring-sky-100"
                value={prompt}
                onChange={(event) => setPrompt(event.target.value)}
                disabled={isCompiling}
                placeholder="Build a task management app with users, projects, tasks, auth, dashboard metrics, and ZIP export."
              />
              <button
                className="mt-3 flex w-full items-center justify-center gap-2 rounded-lg bg-zinc-950 px-4 py-3 text-sm font-semibold text-white transition hover:bg-zinc-800 disabled:cursor-not-allowed disabled:bg-zinc-400"
                onClick={handleCompile}
                disabled={isCompiling || !prompt.trim()}
              >
                {isCompiling ? <Loader2 className="h-4 w-4 animate-spin" /> : <Cpu className="h-4 w-4" />}
                {isCompiling ? 'Compiling' : 'Compile Project'}
              </button>
              {error && (
                <div className="mt-3 flex gap-2 rounded-lg border border-rose-200 bg-rose-50 p-3 text-sm text-rose-800">
                  <AlertTriangle className="mt-0.5 h-4 w-4 shrink-0" />
                  <span>{error}</span>
                </div>
              )}
            </div>

            <div className="rounded-lg border border-zinc-200 bg-white p-4 shadow-sm">
              <div className="mb-3 flex items-center justify-between">
                <h2 className="text-sm font-semibold text-zinc-900">Export Gate</h2>
                <FileArchive className="h-4 w-4 text-zinc-500" />
              </div>
              <div className={`rounded-lg border p-3 text-sm ${exportReady ? 'border-emerald-200 bg-emerald-50 text-emerald-800' : 'border-amber-200 bg-amber-50 text-amber-800'}`}>
                {exportReady ? 'ZIP export approved' : result ? 'ZIP export blocked' : 'Waiting for compilation'}
              </div>
              {exportReady && (
                <a
                  className="mt-3 flex w-full items-center justify-center gap-2 rounded-lg bg-emerald-700 px-4 py-3 text-sm font-semibold text-white transition hover:bg-emerald-600"
                  href={`${API_BASE}${result.download_url}`}
                >
                  <Download className="h-4 w-4" />
                  Download ZIP
                </a>
              )}
            </div>

            <div className="rounded-lg border border-zinc-200 bg-white p-4 shadow-sm">
              <h2 className="mb-3 text-sm font-semibold text-zinc-900">Provider</h2>
              <div className="grid grid-cols-2 gap-2 text-sm">
                <Metric label="Used" value={providerMetrics.last_provider || 'Pending'} />
                <Metric label="Fallbacks" value={providerMetrics.fallbacks ?? 0} />
                <Metric label="Switches" value={providerMetrics.provider_switches ?? 0} />
                <Metric label="Quota" value={providerMetrics.quota_failures ?? 0} />
              </div>
            </div>
          </div>

          <div className="space-y-5">
            <div className="rounded-lg border border-zinc-200 bg-white p-4 shadow-sm">
              <div className="mb-4 flex items-center justify-between">
                <h2 className="text-sm font-semibold text-zinc-900">Pipeline</h2>
                <ShieldCheck className="h-4 w-4 text-emerald-700" />
              </div>
              <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
                {PIPELINE.map((name, index) => {
                  const stage = stageMap.get(name);
                  const status = stage?.status || (isCompiling && index === 0 ? 'running' : 'pending');
                  return (
                    <div key={name} className={`min-h-24 rounded-lg border p-3 ${stageTone(status)}`}>
                      <div className="mb-3 flex items-center justify-between">
                        {statusIcon(status, isCompiling && index === 0)}
                        <span className="text-xs font-semibold uppercase tracking-normal">Stage {index + 1}</span>
                      </div>
                      <div className="text-sm font-semibold">{name}</div>
                      <div className="mt-1 text-xs capitalize opacity-80">{status}</div>
                    </div>
                  );
                })}
              </div>
            </div>

            <div className="grid gap-5 xl:grid-cols-3">
              <div className="rounded-lg border border-zinc-200 bg-white p-4 shadow-sm xl:col-span-2">
                <h2 className="mb-3 text-sm font-semibold text-zinc-900">Runtime Health</h2>
                <div className="space-y-2">
                  {healthChecks.length === 0 ? (
                    <Empty text="No runtime checks yet" />
                  ) : (
                    healthChecks.map((check) => (
                      <div key={check.name} className="flex items-center justify-between rounded-lg border border-zinc-200 px-3 py-2 text-sm">
                        <span className="text-zinc-700">{check.name.replaceAll('_', ' ')}</span>
                        <span className={check.success ? 'text-emerald-700' : 'text-rose-700'}>
                          {check.success ? 'passed' : 'failed'}
                        </span>
                      </div>
                    ))
                  )}
                </div>
              </div>

              <div className="rounded-lg border border-zinc-200 bg-white p-4 shadow-sm">
                <h2 className="mb-3 text-sm font-semibold text-zinc-900">Metrics</h2>
                <div className="grid gap-2 text-sm">
                  <Metric label="Latency" value={formatSeconds(metrics.latency)} />
                  <Metric label="Repairs" value={result?.repair_count ?? 0} />
                  <Metric label="Validation Failures" value={metrics.validation_failures ?? 0} />
                  <Metric label="Runtime Failures" value={metrics.runtime_failures ?? 0} />
                  <Metric label="Quality" value={result?.score?.score ? `${result.score.score}/100` : 'Pending'} />
                </div>
              </div>
            </div>

            <div className="grid gap-5 xl:grid-cols-2">
              <TracePanel
                title="Fallback Events"
                icon={<RefreshCw className="h-4 w-4 text-sky-700" />}
                items={fallbackEvents}
                empty="No fallback events"
                render={(item) => `${item.from || 'provider'} -> ${item.to || 'none'}: ${item.reason}`}
              />
              <TracePanel
                title="Repair Trace"
                icon={<Server className="h-4 w-4 text-emerald-700" />}
                items={repairTrace}
                empty="No repairs recorded"
                render={(item) => `${item.type}: ${item.status || item.error || 'recorded'}`}
              />
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}

function Metric({ label, value }) {
  return (
    <div className="flex min-h-12 items-center justify-between rounded-lg border border-zinc-200 bg-zinc-50 px-3 py-2">
      <span className="text-zinc-500">{label}</span>
      <span className="max-w-40 truncate font-semibold text-zinc-950" title={String(value)}>{value}</span>
    </div>
  );
}

function Empty({ text }) {
  return (
    <div className="rounded-lg border border-dashed border-zinc-300 bg-zinc-50 px-3 py-8 text-center text-sm text-zinc-500">
      {text}
    </div>
  );
}

function TracePanel({ title, icon, items, empty, render }) {
  return (
    <div className="rounded-lg border border-zinc-200 bg-white p-4 shadow-sm">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="text-sm font-semibold text-zinc-900">{title}</h2>
        {icon}
      </div>
      <div className="max-h-52 space-y-2 overflow-auto pr-1">
        {items.length === 0 ? (
          <Empty text={empty} />
        ) : (
          items.map((item, index) => (
            <div key={`${title}-${index}`} className="rounded-lg border border-zinc-200 bg-zinc-50 px-3 py-2 text-xs leading-5 text-zinc-700">
              {render(item)}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;
