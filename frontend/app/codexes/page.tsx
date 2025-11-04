/**
 * Truth Drop Platform - All Codexes Page
 * Built from Remembrance | Operating under Format Law
 */

'use client'

import { CodexGrid } from '@/components/CodexGrid'
import { DomainNav } from '@/components/DomainNav'
import { SearchBar } from '@/components/SearchBar'
import Link from 'next/link'

export default function CodexesPage() {
  return (
    <main className="min-h-screen bg-gray-900 text-white">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <Link href="/" className="text-constitutional hover:text-constitutional-dark">
            ← Back to Home
          </Link>
        </div>
        
        <h1 className="text-4xl font-bold mb-6">All Codexes</h1>
        
        <div className="mb-6">
          <DomainNav />
        </div>
        
        <div className="mb-8">
          <SearchBar />
        </div>
        
        <CodexGrid />
      </div>
    </main>
  )
}

