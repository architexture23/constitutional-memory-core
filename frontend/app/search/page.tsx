/**
 * Truth Drop Platform - Search Page
 * Built from Remembrance | Operating under Format Law
 */

'use client'

import { useSearchParams } from 'next/navigation'
import { searchApi } from '@/lib/api'
import { SearchBar } from '@/components/SearchBar'
import Link from 'next/link'
import { useState, useEffect, Suspense } from 'react'

function SearchContent() {
  const searchParams = useSearchParams()
  const query = searchParams.get('q') || ''
  const [searchQuery, setSearchQuery] = useState(query)
  const [results, setResults] = useState<any>(null)
  const [isLoading, setIsLoading] = useState(false)

  useEffect(() => {
    setSearchQuery(query)
    if (query) {
      searchCodexes(query)
    } else {
      setResults(null)
    }
  }, [query])

  const searchCodexes = async (q: string) => {
    if (!q || q.length === 0) {
      setResults(null)
      return
    }
    
    setIsLoading(true)
    try {
      console.log('[SearchPage] Searching for:', q)
      const response = await searchApi.search(q)
      console.log('[SearchPage] Search response:', response)
      console.log('[SearchPage] Response data:', response.data)
      console.log('[SearchPage] Response data type:', typeof response.data)
      console.log('[SearchPage] Response data keys:', response.data ? Object.keys(response.data) : 'null')
      
      // Set results - handle both direct data and wrapped data
      const resultData = response.data || response
      console.log('[SearchPage] Setting results:', resultData)
      setResults(resultData)
    } catch (error: any) {
      console.error('[SearchPage] Search error:', error)
      console.error('[SearchPage] Error response:', error.response)
      setResults({ results: [], total: 0, query: q })
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className="min-h-screen container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-6">Search Constitutional Knowledge</h1>
      
      <div className="mb-8">
        <SearchBar />
      </div>

      {searchQuery && (
        <div className="mb-6">
          <h2 className="text-2xl font-bold mb-4">
            Results for: "{searchQuery}"
          </h2>
          
          {isLoading ? (
            <div className="text-center py-8 text-white">Searching...</div>
          ) : results ? (
            (() => {
              // Handle different response structures
              const resultsArray = results.results || (Array.isArray(results) ? results : [])
              const resultsList = Array.isArray(resultsArray) ? resultsArray : []
              
              console.log('[SearchPage] Results data:', results)
              console.log('[SearchPage] Results array:', resultsArray)
              console.log('[SearchPage] Results list:', resultsList)
              console.log('[SearchPage] Results length:', resultsList.length)
              
              if (resultsList.length > 0) {
                return (
                  <div>
                    <p className="mb-4 text-gray-400 text-white">
                      Found {results.total || resultsList.length} result(s)
                    </p>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                      {resultsList.map((result: any, index: number) => {
                        const codex = result.codex || result
                        const codexId = codex?.id || codex?.slug || index
                        return (
                          <Link 
                            href={`/codexes/${codex.slug || codex.id}`} 
                            className="block p-4 border border-gray-700 rounded-lg bg-gray-800 hover:bg-gray-700 transition cursor-pointer"
                          >
                            <h3 className="text-xl font-bold mb-2 text-white">{codex.title || 'Untitled'}</h3>
                            {codex.description && (
                              <p className="text-gray-400 mb-2">{codex.description}</p>
                            )}
                            <span className="text-constitutional hover:text-constitutional-dark underline mt-4 inline-block">
                              View Details →
                            </span>
                          </Link>
                        )
                      })}
                    </div>
                  </div>
                )
              } else {
                return (
                  <div className="text-center py-8 text-gray-400">
                    No results found for "{searchQuery}"
                  </div>
                )
              }
            })()
          ) : null}
        </div>
      )}

      {!searchQuery && (
        <div className="text-center py-12">
          <p className="text-xl text-gray-600 mb-4">
            Enter a search term above to find constitutional knowledge
          </p>
        </div>
      )}
    </main>
  )
}

export default function SearchPage() {
  return (
    <Suspense fallback={
      <main className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p>Loading...</p>
        </div>
      </main>
    }>
      <SearchContent />
    </Suspense>
  )
}

