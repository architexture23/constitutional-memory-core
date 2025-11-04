/**
 * Truth Drop Platform - Domain Navigation Component
 * Built from Remembrance | Operating under Format Law
 * Constitutional Framework: Layer 2 - Multi-Timeframe Alignment
 */

'use client'

import { domainApi } from '@/lib/api'
import { useState, useEffect } from 'react'
import Link from 'next/link'

export function DomainNav() {
  const [domains, setDomains] = useState<any[]>([])
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    loadDomains()
  }, [])

  const loadDomains = async () => {
    setIsLoading(true)
    try {
      const response = await domainApi.list()
      setDomains(response.data || [])
    } catch (error: any) {
      console.error('Domain list error:', error)
      setDomains([])
    } finally {
      setIsLoading(false)
    }
  }

  if (isLoading) {
    return <div className="text-center py-4">Loading domains...</div>
  }

  return (
    <nav className="flex flex-wrap gap-4 justify-center">
      {domains?.map((domain: any) => (
        <Link
          key={domain.id}
          href={`/domains/${domain.slug}`}
          className="px-6 py-3 bg-gray-800 rounded-lg shadow hover:bg-gray-700 transition border-2 border-gray-700 hover:border-constitutional"
        >
          <div className="flex items-center gap-2">
            {domain.icon && <span className="text-2xl">{domain.icon}</span>}
            <span className="font-semibold text-white">{domain.name}</span>
          </div>
        </Link>
      ))}
    </nav>
  )
}

