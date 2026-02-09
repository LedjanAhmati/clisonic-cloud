'use client'

import { useState } from 'react'

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
  successful: number
  failed: number
}

const PERSONAS = [
  { id: 'alba', name: 'Alba', emoji: '🌅', role: 'Optimist' },
  { id: 'albi', name: 'Albi', emoji: '🔧', role: 'Pragmatist' },
  { id: 'jona', name: 'Jona', emoji: '🔍', role: 'Skeptic' },
  { id: 'blerina', name: 'Blerina', emoji: '💡', role: 'Analyst' },
  { id: 'asi', name: 'ASI', emoji: '🧠', role: 'Meta-Thinker' },
]

export default function DebatePage() {
  const [topic, setTopic] = useState('')
  const [debate, setDebate] = useState<DebateResult | null>(null)
  const [loading, setLoading] = useState(false)
  const [activeSpeaker, setActiveSpeaker] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const startDebate = async () => {
    if (!topic.trim()) return
    
    setLoading(true)
    setError(null)
    setDebate(null)
    
    for (const p of PERSONAS) {
      setActiveSpeaker(p.id)
      await new Promise(r => setTimeout(r, 600))
    }
    
    try {
      const res = await fetch('/api/debate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic })
      })
      
      if (!res.ok) throw new Error('Debate failed')
      
      const data = await res.json()
      setDebate(data)
    } catch {
      setError('Failed to connect to debate engine')
    } finally {
      setActiveSpeaker(null)
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100">
      {/* Header */}
      <header className="border-b border-zinc-800">
        <div className="max-w-5xl mx-auto px-6 py-5 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-zinc-800 rounded-lg flex items-center justify-center text-lg">
              🎭
            </div>
            <div>
              <h1 className="text-lg font-semibold text-zinc-100">Trinity Debate</h1>
              <p className="text-xs text-zinc-500">5 AI Perspectives • One Topic</p>
            </div>
          </div>
          <a href="/modules" className="text-sm text-zinc-500 hover:text-zinc-300">
            ← Back
          </a>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-6 py-8">
        
        {/* Personas */}
        <div className="grid grid-cols-5 gap-3 mb-8">
          {PERSONAS.map((p) => (
            <div
              key={p.id}
              className={`text-center p-4 rounded-xl border transition-all ${
                activeSpeaker === p.id 
                  ? 'bg-zinc-800 border-zinc-600' 
                  : 'bg-zinc-900 border-zinc-800'
              }`}
            >
              <div className="text-2xl mb-2">{p.emoji}</div>
              <div className="text-sm font-medium text-zinc-200">{p.name}</div>
              <div className="text-xs text-zinc-500">{p.role}</div>
              {activeSpeaker === p.id && (
                <div className="mt-2 flex justify-center">
                  <span className="w-1.5 h-1.5 bg-blue-400 rounded-full animate-pulse" />
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Input */}
        <div className="bg-zinc-900 rounded-xl p-5 border border-zinc-800 mb-6">
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && startDebate()}
            placeholder="Enter a topic for debate..."
            className="w-full bg-transparent text-zinc-100 placeholder-zinc-600 focus:outline-none text-sm"
          />
          <div className="flex items-center justify-between pt-4 mt-4 border-t border-zinc-800">
            <div className="flex flex-wrap gap-2">
              {['Future of AI', 'Remote vs Office', 'Privacy vs Security', 'Climate Action'].map((t) => (
                <button
                  key={t}
                  onClick={() => setTopic(t)}
                  className="px-3 py-1.5 bg-zinc-800 text-zinc-400 text-xs rounded-lg hover:bg-zinc-700 hover:text-zinc-300 transition-colors"
                >
                  {t}
                </button>
              ))}
            </div>
            <button
              onClick={startDebate}
              disabled={loading || !topic.trim()}
              className="px-5 py-2 bg-zinc-100 text-zinc-900 text-sm font-medium rounded-lg hover:bg-white disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
            >
              {loading ? 'Debating...' : 'Start Debate'}
            </button>
          </div>
        </div>

        {/* Error */}
        {error && (
          <div className="bg-red-500/5 border border-red-500/20 rounded-xl p-4 text-red-400 text-sm mb-6">
            {error}
          </div>
        )}

        {/* Debate Results */}
        {debate && (
          <div className="space-y-4">
            <div className="flex items-center justify-between text-sm">
              <span className="text-zinc-400">Topic: <span className="text-zinc-200">{debate.topic}</span></span>
              <span className="text-zinc-600">{debate.successful}/{debate.responses.length} responses</span>
            </div>
            
            {debate.responses.map((r) => (
              <div
                key={r.persona}
                className="bg-zinc-900 rounded-xl p-5 border border-zinc-800"
              >
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-zinc-800 rounded-lg flex items-center justify-center text-xl flex-shrink-0">
                    {r.emoji}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2 mb-2">
                      <span className="font-medium text-zinc-200">{r.name}</span>
                      <span className="text-xs text-zinc-600">{r.role}</span>
                      {r.status === 'error' && (
                        <span className="px-2 py-0.5 bg-red-500/10 text-red-400 text-xs rounded">
                          Error
                        </span>
                      )}
                    </div>
                    <p className="text-zinc-400 text-sm leading-relaxed">
                      {r.response || 'No response'}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Empty */}
        {!debate && !loading && !error && (
          <div className="text-center py-20 text-zinc-600">
            <div className="text-5xl mb-4">🎭</div>
            <p className="text-sm">Enter a topic to start a multi-perspective debate</p>
            <p className="text-xs text-zinc-700 mt-1">5 AI personas will share their unique viewpoints</p>
          </div>
        )}
      </main>
    </div>
  )
}
