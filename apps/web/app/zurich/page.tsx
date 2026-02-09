'use client'
/**
 * ZÜRICH DETERMINISTIC ENGINE
 * ===========================
 * 
 * 9-Stage Logic-Based Reasoning - No AI Randomness
 * From Harmonic Integration
 */

import { useState } from 'react'
import { motion } from 'framer-motion'

interface ZurichResponse {
  ok: boolean
  output: string
  confidence: number
  strategy: string
  domains: string[]
  processing_time_ms: number
  engine: string
}

interface ZurichInfo {
  name: string
  version: string
  type: string
  stages: string[]
  features: string[]
  response_time: string
}

const STAGES = [
  { icon: '📥', name: 'Input Parsing', desc: 'Tokenize and structure the input' },
  { icon: '🏷️', name: 'Classification', desc: 'Identify intent and domain' },
  { icon: '🧩', name: 'Decomposition', desc: 'Break into sub-problems' },
  { icon: '📚', name: 'Knowledge Retrieval', desc: 'Fetch relevant patterns' },
  { icon: '⚙️', name: 'Rule Application', desc: 'Apply domain-specific rules' },
  { icon: '🔗', name: 'Synthesis', desc: 'Combine partial solutions' },
  { icon: '✅', name: 'Validation', desc: 'Check consistency and logic' },
  { icon: '🎨', name: 'Formatting', desc: 'Structure the response' },
  { icon: '📤', name: 'Output Generation', desc: 'Final deterministic output' },
]

export default function ZurichPage() {
  const [query, setQuery] = useState('')
  const [response, setResponse] = useState<ZurichResponse | null>(null)
  const [info, setInfo] = useState<ZurichInfo | null>(null)
  const [loading, setLoading] = useState(false)
  const [activeStage, setActiveStage] = useState(-1)
  const [error, setError] = useState<string | null>(null)

  // Fetch engine info on mount
  useState(() => {
    fetch('/api/zurich/info')
      .then(res => res.json())
      .then(data => setInfo(data))
      .catch(err => console.error('Failed to fetch Zürich info:', err))
  })

  const processQuery = async () => {
    if (!query.trim()) return
    
    setLoading(true)
    setError(null)
    setResponse(null)
    
    // Animate through stages
    for (let i = 0; i < 9; i++) {
      setActiveStage(i)
      await new Promise(r => setTimeout(r, 100))
    }
    
    try {
      const res = await fetch('/api/zurich', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: query })
      })
      
      if (!res.ok) throw new Error('Zürich Engine error')
      
      const data = await res.json()
      setResponse(data)
      setActiveStage(-1)
    } catch (err) {
      setError('Nuk u lidh me Zürich Engine')
      setActiveStage(-1)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-zinc-900 text-white">
      {/* Header */}
      <div className="border-b border-white/10 bg-black/20 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto px-6 py-6">
          <div className="flex items-center gap-4">
            <div className="w-14 h-14 bg-gradient-to-br from-amber-500 to-orange-600 rounded-2xl flex items-center justify-center text-2xl shadow-lg shadow-amber-500/30">
              🎯
            </div>
            <div>
              <h1 className="text-2xl font-bold bg-gradient-to-r from-amber-400 to-orange-400 bg-clip-text text-transparent">
                Zürich Deterministic Engine
              </h1>
              <p className="text-sm text-slate-400">
                {info ? `v${info.version} • ${info.type}` : '9-Stage Logic-Based Reasoning'}
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-6 py-8">
        <div className="grid lg:grid-cols-3 gap-8">
          
          {/* Left: 9-Stage Pipeline */}
          <div className="lg:col-span-1">
            <h2 className="text-lg font-semibold mb-4 text-amber-400">Pipeline Stages</h2>
            <div className="space-y-2">
              {STAGES.map((stage, i) => (
                <motion.div
                  key={i}
                  animate={{
                    scale: activeStage === i ? 1.02 : 1,
                    backgroundColor: activeStage === i ? 'rgba(251, 191, 36, 0.2)' : 'rgba(255,255,255,0.05)'
                  }}
                  className="flex items-center gap-3 p-3 rounded-xl border border-white/10"
                >
                  <span className="text-xl">{stage.icon}</span>
                  <div className="flex-1 min-w-0">
                    <div className="text-sm font-medium">{stage.name}</div>
                    <div className="text-xs text-slate-500 truncate">{stage.desc}</div>
                  </div>
                  {activeStage === i && (
                    <motion.div
                      animate={{ rotate: 360 }}
                      transition={{ repeat: Infinity, duration: 1 }}
                      className="w-4 h-4 border-2 border-amber-400 border-t-transparent rounded-full"
                    />
                  )}
                  {activeStage > i && (
                    <span className="text-green-400">✓</span>
                  )}
                </motion.div>
              ))}
            </div>
          </div>

          {/* Right: Input & Output */}
          <div className="lg:col-span-2 space-y-6">
            
            {/* Input */}
            <div className="bg-white/5 rounded-2xl p-6 border border-white/10">
              <h2 className="text-lg font-semibold mb-4">Query Input</h2>
              <textarea
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Shkruaj pyetjen tënde këtu... p.sh. 'Si të ndërtoj një startup AI të suksesshëm?'"
                className="w-full h-32 bg-black/30 border border-white/20 rounded-xl p-4 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-amber-500/50 resize-none"
              />
              <div className="flex items-center justify-between mt-4">
                <div className="text-sm text-slate-500">
                  {query.length} karaktere
                </div>
                <button
                  onClick={processQuery}
                  disabled={loading || !query.trim()}
                  className="px-6 py-2.5 bg-gradient-to-r from-amber-500 to-orange-600 text-white font-medium rounded-xl hover:shadow-lg hover:shadow-amber-500/30 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {loading ? 'Duke procesuar...' : '🎯 Proceso me Zürich'}
                </button>
              </div>
            </div>

            {/* Error */}
            {error && (
              <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 text-red-400">
                {error}
              </div>
            )}

            {/* Output */}
            {response && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white/5 rounded-2xl p-6 border border-white/10"
              >
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-lg font-semibold">Rezultati</h2>
                  <div className="flex items-center gap-4 text-sm">
                    <span className="text-amber-400">
                      ⚡ {response.processing_time_ms.toFixed(2)}ms
                    </span>
                    <span className="text-green-400">
                      🎯 {(response.confidence * 100).toFixed(0)}% konfidencë
                    </span>
                  </div>
                </div>
                
                {/* Metadata */}
                <div className="flex flex-wrap gap-2 mb-4">
                  <span className="px-2 py-1 bg-amber-500/20 text-amber-400 text-xs rounded-lg">
                    Strategjia: {response.strategy}
                  </span>
                  {response.domains.map(d => (
                    <span key={d} className="px-2 py-1 bg-blue-500/20 text-blue-400 text-xs rounded-lg">
                      {d}
                    </span>
                  ))}
                </div>

                {/* Output content */}
                <div className="bg-black/30 rounded-xl p-4 prose prose-invert prose-sm max-w-none">
                  <pre className="whitespace-pre-wrap text-slate-300 font-mono text-sm">
                    {response.output}
                  </pre>
                </div>
              </motion.div>
            )}

            {/* Features */}
            {info && (
              <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
                {info.features.map((f, i) => (
                  <div key={i} className="bg-white/5 rounded-xl p-3 border border-white/10 text-center">
                    <div className="text-xs text-slate-400">{f}</div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
