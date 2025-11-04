/**
 * Truth Drop Platform - Codex Card Component
 * Built from Remembrance | Operating under Format Law
 */

'use client'

import Link from 'next/link'

interface CodexCardProps {
  codex: {
    id: number
    slug: string
    title: string
    description?: string
    price?: number | null
    currency?: string
    domain?: {
      name: string
      color?: string
    }
    is_featured?: boolean
  }
}

export function CodexCard({ codex }: CodexCardProps) {
  return (
    <Link href={`/codexes/${codex.slug}`}>
      <div className="bg-gray-800 rounded-lg p-6 hover:bg-gray-700 transition cursor-pointer h-full flex flex-col">
        {codex.is_featured && (
          <span className="inline-block px-2 py-1 mb-2 text-xs font-semibold bg-constitutional/20 text-constitutional rounded">
            Featured
          </span>
        )}
        
        <h3 className="text-xl font-bold mb-2 text-white">{codex.title}</h3>
        
        {codex.description && (
          <p className="text-gray-400 mb-4 flex-grow">{codex.description}</p>
        )}
        
        {codex.domain && (
          <div className="mb-4">
            <span 
              className="px-2 py-1 text-xs rounded"
              style={{ 
                backgroundColor: codex.domain.color ? `${codex.domain.color}20` : 'rgba(139, 92, 246, 0.2)',
                color: codex.domain.color || '#8B5CF6'
              }}
            >
              {codex.domain.name}
            </span>
          </div>
        )}
        
        {codex.price !== null && codex.price !== undefined && (
          <div className="mt-auto">
            <span className="text-2xl font-bold text-white">
              ${codex.price.toFixed(2)}
            </span>
            {codex.currency && codex.currency !== 'USD' && (
              <span className="text-gray-400 ml-1">{codex.currency}</span>
            )}
          </div>
        )}
        
        {(!codex.price || codex.price === 0) && (
          <div className="mt-auto">
            <span className="text-lg font-semibold text-green-400">Free</span>
          </div>
        )}
      </div>
    </Link>
  )
}
