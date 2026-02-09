'use client'
/**
 * TRINITY DEBATE - Multi-Persona AI Discussion
 * =============================================
 * 
 * 5 AI Personas debate any topic
 * From Harmonic Integration
 */

import { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'

interface Persona {
  id: string
  name: string
  emoji: string
  role: string
  style: string
  focus: string
}

interface DebateResponse {
  persona: string
  name: string
  emoji: string
  role: string
  response: string
  status: 'success' | 'error'
}

interface DebateResult {
  ok: boolean
  topic: string
  responses: DebateResponse[]
  total_responses: number
  successful: number
  failed: number
}

const PERSONA_COLORS: Record<string, string> = {
  alba: 'from-amber-500 to-orange-500',
  albi: 'from-slate-500 to-zinc-600',
  jona: 'from-purple-500 to-indigo-600',
  blerina: 'from-pink-500 to-rose-600',
  asi: 'from-cyan-500 to-blue-600',
}

const PERSONA_BG: Record<string, string> = {
  alba: 'bg-amber-500/10 border-amber-500/30',
  albi: 'bg-slate-500/10 border-slate-500/30',
  jona: 'bg-purple-500/10 border-purple-500/30',
  blerina: 'bg-pink-500/10 border-pink-500/30',
  asi: 'bg-cyan-500/10 border-cyan-500/30',
}

export default function DebatePage() {
  const [topic, setTopic] = useState('')
  const [personas, setPersonas] = useState<Persona[]>([])
  const [debate, setDebate] = useState<DebateResult | null>(null)
  const [loading, setLoading] = useState(false)
  const [currentSpeaker, setCurrentSpeaker] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)
  const debateRef = useRef<HTMLDivElement>(null)

  // Fetch personas on mount
  useEffect(() => {
    fetch('/api/debate/personas')
      .then(res => res.json())
      .then(data => setPersonas(data.personas || []))
      .catch(err => console.error('Failed to fetch personas:', err))
  }, [])

  const startDebate = async () => {
    if (!topic.trim()) return
    
    setLoading(true)
    setError(null)
    setDebate(null)
    
    // Animate speakers
    const speakerOrder = ['alba', 'albi', 'jona', 'blerina', 'asi']
    for (const speaker of speakerOrder) {
      setCurrentSpeaker(speaker)
      await new Promise(r => setTimeout(r, 800))
    }
    
    try {
      const res = await fetch('/api/debate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic })
      })
      
      if (!res.ok) throw new Error('Debate Engine error')
      
      const data = await res.json()
      setDebate(data)
      setCurrentSpeaker(null)
      
      // Scroll to debate
      setTimeout(() => {
        debateRef.current?.scrollIntoView({ behavior: 'smooth' })
      }, 100)
    } catch (err) {
      setError('Nuk u lidh me Trinity Debate Engine')
      setCurrentSpeaker(null)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900/20 to-slate-900 text-white">
      {/* Header */}
      <div className="border-b border-white/10 bg-black/20 backdrop-blur-xl">
        <div className="max-w-7xl mx-auto px-6 py-6">
          <div className="flex items-center gap-4">
            <div className="w-14 h-14 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-2xl flex items-center justify-center text-2xl shadow-lg shadow-purple-500/30">
              🎭
            </div>
            <div>
              <h1 className="text-2xl font-bold bg-gradient-to-r from-purple-400 to-indigo-400 bg-clip-text text-transparent">
                Trinity Debate Engine
              </h1>
              <p className="text-sm text-slate-400">
                5 AI Personas • Multi-Perspective Discussion
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-6 py-8">
        
        {/* Personas Grid */}
        <div className="mb-8">
          <h2 className="text-lg font-semibold mb-4 text-purple-400">The Council</h2>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
            {personas.map((p) => (
              <motion.div
                key={p.id}
                animate={{
                  scale: currentSpeaker === p.id ? 1.05 : 1,
                  boxShadow: currentSpeaker === p.id ? '0 0 30px rgba(168, 85, 247, 0.4)' : 'none'
                }}
                className={`relative p-4 rounded-2xl border ${PERSONA_BG[p.id] || 'bg-white/5 border-white/10'} text-center transition-all`}
              >
                {currentSpeaker === p.id && (
                  <motion.div
                    animate={{ opacity: [0.5, 1, 0.5] }}
                    transition={{ repeat: Infinity, duration: 1.5 }}
                    className="absolute inset-0 bg-gradient-to-br from-purple-500/20 to-transparent rounded-2xl"
                  />
                )}
                <div className="text-4xl mb-2">{p.emoji}</div>
                <div className="font-semibold">{p.name}</div>
                <div className="text-xs text-slate-400">{p.role}</div>
                {currentSpeaker === p.id && (
                  <div className="absolute -top-2 -right-2 w-6 h-6 bg-purple-500 rounded-full flex items-center justify-center text-xs animate-pulse">
                    🎤
                  </div>
                )}
              </motion.div>
            ))}
          </div>
        </div>

        {/* Topic Input */}
        <div className="bg-white/5 rounded-2xl p-6 border border-white/10 mb-8">
          <h2 className="text-lg font-semibold mb-4">Tema e Debatit</h2>
          <div className="flex gap-4">
            <input
              type="text"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && startDebate()}
              placeholder="Shkruaj një temë për debat... p.sh. 'A duhet AI të zëvendësojë punët e njerëzve?'"
              className="flex-1 bg-black/30 border border-white/20 rounded-xl px-4 py-3 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500/50"
            />
            <button
              onClick={startDebate}
              disabled={loading || !topic.trim()}
              className="px-6 py-3 bg-gradient-to-r from-purple-500 to-indigo-600 text-white font-medium rounded-xl hover:shadow-lg hover:shadow-purple-500/30 transition-all disabled:opacity-50 disabled:cursor-not-allowed whitespace-nowrap"
            >
              {loading ? 'Duke debatuar...' : '🎭 Fillo Debatin'}
            </button>
          </div>
          
          {/* Quick topics */}
          <div className="flex flex-wrap gap-2 mt-4">
            {[
              'A është AI e rrezikshme?',
              'Ardhmëria e punës',
              'Klima vs Ekonomia',
              'Edukimi tradicional vs Online',
              'Privatësia në epokën dixhitale'
            ].map((t) => (
              <button
                key={t}
                onClick={() => setTopic(t)}
                className="px-3 py-1.5 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-sm text-slate-400 hover:text-white transition-all"
              >
                {t}
              </button>
            ))}
          </div>
        </div>

        {/* Error */}
        {error && (
          <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 text-red-400 mb-8">
            {error}
          </div>
        )}

        {/* Debate Results */}
        {debate && (
          <div ref={debateRef} className="space-y-4">
            <div className="flex items-center justify-between">
              <h2 className="text-lg font-semibold text-purple-400">
                📜 Debati: "{debate.topic}"
              </h2>
              <div className="text-sm text-slate-400">
                {debate.successful}/{debate.total_responses} përgjigje
              </div>
            </div>
            
            <AnimatePresence>
              {debate.responses.map((r, i) => (
                <motion.div
                  key={r.persona}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: i * 0.1 }}
                  className={`rounded-2xl p-5 border ${PERSONA_BG[r.persona] || 'bg-white/5 border-white/10'}`}
                >
                  <div className="flex items-start gap-4">
                    {/* Avatar */}
                    <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${PERSONA_COLORS[r.persona] || 'from-gray-500 to-gray-600'} flex items-center justify-center text-2xl flex-shrink-0`}>
                      {r.emoji}
                    </div>
                    
                    {/* Content */}
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2 mb-2">
                        <span className="font-semibold">{r.name}</span>
                        <span className="text-xs text-slate-500">• {r.role}</span>
                        {r.status === 'error' && (
                          <span className="px-2 py-0.5 bg-red-500/20 text-red-400 text-xs rounded">
                            Gabim
                          </span>
                        )}
                      </div>
                      <div className="text-slate-300 text-sm leading-relaxed whitespace-pre-wrap">
                        {r.response || 'Nuk ka përgjigje'}
                      </div>
                    </div>
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>
          </div>
        )}

        {/* Empty state */}
        {!debate && !loading && (
          <div className="text-center py-16">
            <div className="text-6xl mb-4">🎭</div>
            <h3 className="text-xl font-semibold mb-2">Filloni një Debat</h3>
            <p className="text-slate-400 max-w-md mx-auto">
              Shkruani një temë dhe 5 persona AI do të diskutojnë nga këndvështrime të ndryshme.
              Secili sjell perspektivën e tij unike.
            </p>
          </div>
        )}
      </div>
    </div>
  )
}
