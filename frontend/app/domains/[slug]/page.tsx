/**
 * Truth Drop Platform - Domain Codexes Page
 * Built from Remembrance | Operating under Format Law
 */

'use client'

import { CodexGrid } from '@/components/CodexGrid'
import { DomainNav } from '@/components/DomainNav'
import { notFound } from 'next/navigation'
import Link from 'next/link'
import { use } from 'react'

export default function DomainPage({ params }: { params: Promise<{ slug: string }> | { slug: string } }) {
  // Handle both Promise and direct params (Next.js 14 compatibility)
  const resolvedParams = params instanceof Promise ? use(params) : params
  const domainSlug = resolvedParams.slug

  // Map slug to domain name
  const domainMap: { [key: string]: string } = {
    'trading': 'Trading',
    'aura-academy': 'Aura Academy',
    'remembrance-infrastructure': 'Remembrance Infrastructure'
  }

  const domainName = domainMap[domainSlug.toLowerCase()]
  
  if (!domainName) {
    notFound()
  }

  return (
    <main className="min-h-screen bg-gray-900 text-white">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <Link href="/" className="text-constitutional hover:text-constitutional-dark">
            ← Back to Home
          </Link>
        </div>
        
        <h1 className="text-4xl font-bold mb-6">{domainName} Codexes</h1>
        
        <div className="mb-6">
          <DomainNav />
        </div>
        
        <CodexGrid domain={domainName} />
      </div>
    </main>
  )
}

