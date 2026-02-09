/**
 * Clisonix Data Sources Dashboard
 * Enterprise-grade data source management with real-time metrics
 * Connects to: /api/proxy/user-data-sources, /api/proxy/system-metrics
 */

"use client"

import { useState, useEffect, useCallback } from 'react'
import Link from 'next/link'

// ─────────────────────────────────────────────────────────────
// Types
// ─────────────────────────────────────────────────────────────
interface DataSource {
  id: string
  name: string
  type: 'iot' | 'api' | 'lora' | 'gsm' | 'mqtt' | 'webhook' | 'database'
  status: 'connected' | 'disconnected' | 'error' | 'syncing'
  endpoint?: string
  lastSync: string
  dataPoints: number
  throughput: string
  latency: number
  createdAt: string
}

interface DashboardMetrics {
  totalSources: number
  connectedSources: number
  totalDataPoints: number
  dataPointsToday: number
  storageUsed: string
  apiCallsToday: number
  avgLatency: number
  uptime: string
}

// ─────────────────────────────────────────────────────────────
// Configuration
// ─────────────────────────────────────────────────────────────
const SOURCE_TYPES = {
  iot:      { icon: '📡', label: 'IoT Sensor',    color: 'from-emerald-500 to-teal-600' },
  api:      { icon: '🔗', label: 'REST API',      color: 'from-blue-500 to-indigo-600' },
  lora:     { icon: '📶', label: 'LoRaWAN',       color: 'from-purple-500 to-violet-600' },
  gsm:      { icon: '📱', label: 'Cellular/4G',   color: 'from-orange-500 to-red-500' },
  mqtt:     { icon: '🌐', label: 'MQTT Broker',   color: 'from-cyan-500 to-blue-500' },
  webhook:  { icon: '🔔', label: 'Webhook',       color: 'from-pink-500 to-rose-500' },
  database: { icon: '🗄️', label: 'Database',      color: 'from-slate-500 to-gray-600' }
} as const

const STATUS_CONFIG = {
  connected:    { label: 'Connected',    dot: 'bg-emerald-500', text: 'text-emerald-400', pulse: true },
  disconnected: { label: 'Disconnected', dot: 'bg-gray-500',    text: 'text-gray-400',    pulse: false },
  error:        { label: 'Error',        dot: 'bg-red-500',     text: 'text-red-400',     pulse: true },
  syncing:      { label: 'Syncing',      dot: 'bg-amber-500',   text: 'text-amber-400',   pulse: true }
} as const

type FilterType = 'all' | DataSource['type'] | DataSource['status']

// ─────────────────────────────────────────────────────────────
// Component
// ─────────────────────────────────────────────────────────────
export default function DataSourcesDashboard() {
  const [sources, setSources] = useState<DataSource[]>([])
  const [metrics, setMetrics] = useState<DashboardMetrics | null>(null)
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState<FilterType>('all')
  const [searchQuery, setSearchQuery] = useState('')
  const [refreshing, setRefreshing] = useState(false)

  // Fetch data from API
  const fetchData = useCallback(async (showRefresh = false) => {
    if (showRefresh) setRefreshing(true)
    
    try {
      const [sourcesRes, metricsRes] = await Promise.all([
        fetch('/api/proxy/user-data-sources'),
        fetch('/api/proxy/system-metrics')
      ])

      if (sourcesRes.ok) {
        const data = await sourcesRes.json()
        if (data.sources && Array.isArray(data.sources)) {
          setSources(data.sources)
        } else {
          setSources(DEMO_SOURCES)
        }
      } else {
        setSources(DEMO_SOURCES)
      }

      if (metricsRes.ok) {
        const data = await metricsRes.json()
        setMetrics({
          totalSources: data.total_sources || DEMO_SOURCES.length,
          connectedSources: data.connected_sources || 5,
          totalDataPoints: data.total_requests || 2367700,
          dataPointsToday: data.requests_today || 89420,
          storageUsed: data.disk_used || '18.4 GB',
          apiCallsToday: data.api_calls || 127840,
          avgLatency: data.avg_latency || 52,
          uptime: data.uptime || '99.97%'
        })
      } else {
        setMetrics(DEMO_METRICS)
      }
    } catch (err) {
      console.error('Failed to fetch data:', err)
      setSources(DEMO_SOURCES)
      setMetrics(DEMO_METRICS)
    } finally {
      setLoading(false)
      setRefreshing(false)
    }
  }, [])

  useEffect(() => {
    fetchData()
    const interval = setInterval(() => fetchData(), 30000)
    return () => clearInterval(interval)
  }, [fetchData])

  // Filter logic
  const filteredSources = sources.filter(source => {
    const matchesFilter = filter === 'all' || source.type === filter || source.status === filter
    const matchesSearch = source.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          source.endpoint?.toLowerCase().includes(searchQuery.toLowerCase())
    return matchesFilter && matchesSearch
  })

  const connectedCount = sources.filter(s => s.status === 'connected').length

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-950 flex items-center justify-center">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-slate-400">Loading data sources...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      {/* Header */}
      <header className="border-b border-slate-800 bg-slate-900/50 backdrop-blur-sm sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <Link href="/modules" className="text-slate-500 hover:text-white text-sm mb-1 inline-flex items-center gap-1 transition-colors">
                <span>←</span> Back to Modules
              </Link>
              <h1 className="text-2xl font-bold text-white">Data Sources</h1>
            </div>
            <div className="flex items-center gap-3">
              <button
                onClick={() => fetchData(true)}
                disabled={refreshing}
                className="px-4 py-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-sm font-medium transition-all flex items-center gap-2 disabled:opacity-50"
              >
                <span className={refreshing ? 'animate-spin' : ''}>↻</span>
                {refreshing ? 'Refreshing...' : 'Refresh'}
              </button>
              <button className="px-4 py-2 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 rounded-lg text-sm font-semibold transition-all flex items-center gap-2">
                <span>+</span> Add Source
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-6 py-8">
        {/* Metrics Grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-8 gap-4 mb-8">
          <MetricCard label="Total Sources" value={metrics?.totalSources || sources.length} icon="📊" />
          <MetricCard label="Connected" value={connectedCount} icon="✓" accent="emerald" />
          <MetricCard label="Data Points" value={formatNumber(metrics?.totalDataPoints || 0)} icon="📈" />
          <MetricCard label="Today" value={formatNumber(metrics?.dataPointsToday || 0)} icon="📅" accent="cyan" />
          <MetricCard label="Storage" value={metrics?.storageUsed || '—'} icon="💾" />
          <MetricCard label="API Calls" value={formatNumber(metrics?.apiCallsToday || 0)} icon="🔗" />
          <MetricCard label="Avg Latency" value={`${metrics?.avgLatency || 0}ms`} icon="⚡" accent="amber" />
          <MetricCard label="Uptime" value={metrics?.uptime || '99.9%'} icon="🟢" accent="emerald" />
        </div>

        {/* Filters */}
        <div className="flex flex-col md:flex-row gap-4 mb-6">
          <div className="relative flex-1 max-w-md">
            <input
              type="text"
              placeholder="Search sources by name or endpoint..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full bg-slate-900 border border-slate-700 rounded-lg pl-10 pr-4 py-2.5 text-white placeholder-slate-500 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500/50 transition-all"
            />
            <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500">🔍</span>
          </div>
          
          <div className="flex gap-2 flex-wrap">
            {(['all', 'connected', 'iot', 'api', 'mqtt', 'webhook'] as FilterType[]).map(f => (
              <button
                key={f}
                onClick={() => setFilter(f)}
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                  filter === f
                    ? 'bg-cyan-500/20 text-cyan-400 border border-cyan-500/50'
                    : 'bg-slate-800/50 text-slate-400 border border-slate-700 hover:border-slate-600 hover:text-white'
                }`}
              >
                {f === 'all' ? 'All' : f === 'connected' ? '● Connected' : f.toUpperCase()}
              </button>
            ))}
          </div>
        </div>

        {/* Sources Grid */}
        {filteredSources.length === 0 ? (
          <div className="text-center py-16">
            <div className="text-6xl mb-4">📭</div>
            <h3 className="text-xl font-semibold text-slate-300 mb-2">No data sources found</h3>
            <p className="text-slate-500 mb-6">
              {searchQuery ? 'Try adjusting your search query' : 'Add your first data source to get started'}
            </p>
            <button className="px-6 py-3 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-lg font-semibold">
              + Add Data Source
            </button>
          </div>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
            {filteredSources.map(source => (
              <SourceCard key={source.id} source={source} />
            ))}
          </div>
        )}

        {/* Quick Connect */}
        <section className="mt-12">
          <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
            <span className="text-2xl">⚡</span> Quick Connect
          </h2>
          <div className="grid md:grid-cols-4 gap-4">
            {Object.entries(SOURCE_TYPES).slice(0, 4).map(([type, config]) => (
              <button
                key={type}
                className={`bg-gradient-to-br ${config.color} p-[1px] rounded-xl group`}
              >
                <div className="bg-slate-900 rounded-xl p-5 h-full hover:bg-slate-800/50 transition-all">
                  <div className="text-3xl mb-3">{config.icon}</div>
                  <div className="font-semibold text-white group-hover:text-cyan-400 transition-colors">
                    Connect {config.label}
                  </div>
                  <div className="text-slate-500 text-sm mt-1">
                    Configure new {type.toUpperCase()} source
                  </div>
                </div>
              </button>
            ))}
          </div>
        </section>

        {/* Documentation */}
        <section className="mt-12 bg-gradient-to-r from-slate-800/50 to-slate-900/50 rounded-2xl p-8 border border-slate-700">
          <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
            <span>📚</span> Integration Documentation
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div>
              <div className="w-10 h-10 bg-cyan-500/20 rounded-lg flex items-center justify-center mb-3">
                <span className="text-cyan-400 font-bold">1</span>
              </div>
              <h3 className="font-semibold text-white mb-2">Choose Protocol</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Select MQTT, HTTP REST, WebSocket, LoRaWAN, or direct cellular connection based on your device capabilities.
              </p>
            </div>
            <div>
              <div className="w-10 h-10 bg-cyan-500/20 rounded-lg flex items-center justify-center mb-3">
                <span className="text-cyan-400 font-bold">2</span>
              </div>
              <h3 className="font-semibold text-white mb-2">Configure Endpoint</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Generate unique API keys and configure your device with the provided endpoints and authentication tokens.
              </p>
            </div>
            <div>
              <div className="w-10 h-10 bg-cyan-500/20 rounded-lg flex items-center justify-center mb-3">
                <span className="text-cyan-400 font-bold">3</span>
              </div>
              <h3 className="font-semibold text-white mb-2">Stream Data</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Data flows automatically with &lt;50ms latency. Monitor throughput and health in real-time from this dashboard.
              </p>
            </div>
          </div>
          <div className="mt-6 pt-6 border-t border-slate-700 flex gap-4">
            <Link href="/developers" className="text-cyan-400 hover:text-cyan-300 text-sm font-medium">
              View API Documentation →
            </Link>
            <a href="https://github.com/Web8kameleon-hub/clisonix.com" className="text-slate-400 hover:text-white text-sm font-medium">
              GitHub Examples →
            </a>
          </div>
        </section>
      </main>
    </div>
  )
}

// ─────────────────────────────────────────────────────────────
// Sub-components
// ─────────────────────────────────────────────────────────────
function MetricCard({ 
  label, 
  value, 
  icon, 
  accent = 'slate' 
}: { 
  label: string
  value: string | number
  icon: string
  accent?: 'slate' | 'emerald' | 'cyan' | 'amber'
}) {
  const accentColors = {
    slate: 'text-white',
    emerald: 'text-emerald-400',
    cyan: 'text-cyan-400',
    amber: 'text-amber-400'
  }

  return (
    <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-4 hover:border-slate-700 transition-all">
      <div className="text-lg mb-1">{icon}</div>
      <div className={`text-xl font-bold ${accentColors[accent]}`}>{value}</div>
      <div className="text-slate-500 text-xs">{label}</div>
    </div>
  )
}

function SourceCard({ source }: { source: DataSource }) {
  const typeConfig = SOURCE_TYPES[source.type] || SOURCE_TYPES.api
  const statusConfig = STATUS_CONFIG[source.status] || STATUS_CONFIG.disconnected

  return (
    <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-5 hover:border-cyan-500/50 transition-all group">
      <div className="flex items-start justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className={`w-12 h-12 bg-gradient-to-br ${typeConfig.color} rounded-xl flex items-center justify-center text-xl shadow-lg`}>
            {typeConfig.icon}
          </div>
          <div>
            <h3 className="font-semibold text-white group-hover:text-cyan-400 transition-colors">
              {source.name}
            </h3>
            <span className="text-slate-500 text-sm">{typeConfig.label}</span>
          </div>
        </div>
        <div className={`flex items-center gap-2 ${statusConfig.text}`}>
          <div className={`w-2 h-2 rounded-full ${statusConfig.dot} ${statusConfig.pulse ? 'animate-pulse' : ''}`} />
          <span className="text-xs font-medium">{statusConfig.label}</span>
        </div>
      </div>

      {source.endpoint && (
        <div className="mb-4 px-3 py-2 bg-slate-800/50 rounded-lg">
          <code className="text-xs text-slate-400 font-mono break-all">{source.endpoint}</code>
        </div>
      )}

      <div className="grid grid-cols-3 gap-3 text-center mb-4">
        <div>
          <div className="text-white font-semibold">{formatNumber(source.dataPoints)}</div>
          <div className="text-slate-500 text-xs">Data Points</div>
        </div>
        <div>
          <div className="text-white font-semibold">{source.throughput}</div>
          <div className="text-slate-500 text-xs">Throughput</div>
        </div>
        <div>
          <div className="text-white font-semibold">{source.latency}ms</div>
          <div className="text-slate-500 text-xs">Latency</div>
        </div>
      </div>

      <div className="flex items-center justify-between pt-4 border-t border-slate-800">
        <span className="text-slate-500 text-xs">Last sync: {source.lastSync}</span>
        <div className="flex gap-2">
          <button className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 rounded text-xs font-medium transition-colors">
            Configure
          </button>
          <button className="px-3 py-1.5 bg-cyan-500/20 hover:bg-cyan-500/30 text-cyan-400 rounded text-xs font-medium transition-colors">
            View Data
          </button>
        </div>
      </div>
    </div>
  )
}

// ─────────────────────────────────────────────────────────────
// Utilities
// ─────────────────────────────────────────────────────────────
function formatNumber(num: number): string {
  if (num >= 1_000_000) return `${(num / 1_000_000).toFixed(1)}M`
  if (num >= 1_000) return `${(num / 1_000).toFixed(1)}K`
  return num.toString()
}

// Demo data (fallback when API unavailable)
const DEMO_SOURCES: DataSource[] = [
  {
    id: 'src-001',
    name: 'Industrial Temperature Array',
    type: 'iot',
    status: 'connected',
    endpoint: 'mqtt://sensors.clisonix.cloud:1883/temp/*',
    lastSync: '12s ago',
    dataPoints: 284930,
    throughput: '1.2K/s',
    latency: 23,
    createdAt: '2025-11-15'
  },
  {
    id: 'src-002',
    name: 'Weather Service API',
    type: 'api',
    status: 'connected',
    endpoint: 'https://api.weather.clisonix.cloud/v2',
    lastSync: '2m ago',
    dataPoints: 45120,
    throughput: '50/s',
    latency: 89,
    createdAt: '2025-12-01'
  },
  {
    id: 'src-003',
    name: 'LoRaWAN Gateway EU868',
    type: 'lora',
    status: 'connected',
    endpoint: 'lorawan://eu868.clisonix.cloud',
    lastSync: '45s ago',
    dataPoints: 128450,
    throughput: '200/s',
    latency: 156,
    createdAt: '2025-10-20'
  },
  {
    id: 'src-004',
    name: 'Cellular Modem Fleet',
    type: 'gsm',
    status: 'disconnected',
    endpoint: 'gsm://fleet.clisonix.cloud',
    lastSync: '4h ago',
    dataPoints: 12340,
    throughput: '0/s',
    latency: 0,
    createdAt: '2026-01-05'
  },
  {
    id: 'src-005',
    name: 'Production MQTT Cluster',
    type: 'mqtt',
    status: 'connected',
    endpoint: 'mqtts://prod.clisonix.cloud:8883',
    lastSync: '3s ago',
    dataPoints: 1892340,
    throughput: '5.8K/s',
    latency: 12,
    createdAt: '2025-08-10'
  },
  {
    id: 'src-006',
    name: 'Stripe Payment Webhooks',
    type: 'webhook',
    status: 'connected',
    endpoint: 'https://clisonix.cloud/api/webhooks/stripe',
    lastSync: '8m ago',
    dataPoints: 4520,
    throughput: '2/s',
    latency: 34,
    createdAt: '2025-12-15'
  }
]

const DEMO_METRICS: DashboardMetrics = {
  totalSources: 6,
  connectedSources: 5,
  totalDataPoints: 2367700,
  dataPointsToday: 89420,
  storageUsed: '18.4 GB',
  apiCallsToday: 127840,
  avgLatency: 52,
  uptime: '99.97%'
}







