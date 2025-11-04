/**
 * Truth Drop Platform - Codex Grid Component
 * Built from Remembrance | Operating under Format Law
 */

'use client'

import { codexApi } from '@/lib/api'
import { useState, useEffect } from 'react'
import { CodexCard } from './CodexCard'

interface CodexGridProps {
  featured?: boolean
  domain?: string
  limit?: number
}

export function CodexGrid({ featured, domain, limit }: CodexGridProps) {
  const [codexes, setCodexes] = useState<any[]>([])
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    loadCodexes()
  }, [featured, domain, limit])

  const loadCodexes = async () => {
    setIsLoading(true)
    try {
      const params: any = { limit: limit || 50 }
      if (domain) params.domain = domain
      if (featured !== undefined && featured !== null) {
        params.featured = featured === true
      }
      
      console.log('[CodexGrid] Loading codexes with params:', params)
      console.log('[CodexGrid] API URL:', process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000')
      const response = await codexApi.list(params)
      console.log('[CodexGrid] API response:', response)
      console.log('[CodexGrid] Response data:', response.data)
      console.log('[CodexGrid] Response data type:', typeof response.data)
      console.log('[CodexGrid] Is array:', Array.isArray(response.data))
      
      // Handle response - axios wraps response.data
      let codexArray = []
      if (Array.isArray(response.data)) {
        codexArray = response.data
      } else if (response.data && typeof response.data === 'object' && 'data' in response.data) {
        // Handle nested data
        codexArray = Array.isArray(response.data.data) ? response.data.data : []
      }
      
      console.log('[CodexGrid] Loaded codexes:', codexArray.length, codexArray)
      
      if (codexArray.length > 0) {
        console.log('[CodexGrid] First codex:', codexArray[0])
      }
      
      setCodexes(codexArray)
    } catch (error: any) {
      console.error('[CodexGrid] Error loading codexes:', error)
      console.error('[CodexGrid] Error response:', error.response)
      console.error('[CodexGrid] Error message:', error.message)
      setCodexes([])
    } finally {
      setIsLoading(false)
    }
  }

  if (isLoading) {
    return <div className="text-center py-8">Loading codexes...</div>
  }

  if (!codexes || codexes.length === 0) {
    return <div className="text-center py-8 text-gray-500">No codexes found</div>
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {codexes.map((codex: any) => (
        <CodexCard key={codex.id} codex={codex} />
      ))}
    </div>
  )
}

