/**
 * Truth Drop Platform - Search Bar Component
 * Built from Remembrance | Operating under Format Law
 * Constitutional Framework: Layer 3 - Liquidity Manipulation (Pattern Discovery)
 */

'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { Search } from 'lucide-react'

export function SearchBar() {
  const [query, setQuery] = useState('')
  const router = useRouter()

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    if (query.trim()) {
      router.push(`/search?q=${encodeURIComponent(query)}`)
    }
  }

  return (
    <form onSubmit={handleSearch} className="max-w-2xl mx-auto">
      <div className="flex gap-2">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search constitutional knowledge..."
          className="flex-1 px-4 py-3 border-2 border-gray-300 rounded-lg focus:border-constitutional focus:outline-none text-gray-900 bg-white placeholder-gray-400"
        />
        <button
          type="submit"
          className="px-6 py-3 bg-constitutional text-white rounded-lg font-semibold hover:bg-constitutional-dark transition flex items-center gap-2"
        >
          <Search size={20} />
          Search
        </button>
      </div>
    </form>
  )
}

