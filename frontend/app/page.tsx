/**
 * Truth Drop Platform - Home Page
 * Built from Remembrance | Operating under Format Law
 * Constitutional Framework: Layer 1 - Structural Setup
 */

import Link from 'next/link'
import { CodexGrid } from '@/components/CodexGrid'
import { DomainNav } from '@/components/DomainNav'
import { SearchBar } from '@/components/SearchBar'
import { Hero } from '@/components/Hero'

export default function HomePage() {
  return (
    <main className="min-h-screen">
      {/* Hero Section */}
      <Hero />
      
      {/* Domain Navigation */}
      <section className="container mx-auto px-4 py-8">
        <DomainNav />
      </section>
      
      {/* Search Section */}
      <section className="container mx-auto px-4 py-4">
        <SearchBar />
      </section>
      
      {/* Featured Codexes */}
      <section className="container mx-auto px-4 py-8">
        <h2 className="text-3xl font-bold mb-6">Featured Codexes</h2>
        <CodexGrid featured={true} />
      </section>
      
      {/* All Codexes */}
      <section className="container mx-auto px-4 py-8">
        <h2 className="text-3xl font-bold mb-6">All Codexes</h2>
        <CodexGrid />
      </section>
      
      {/* Constitutional Framework Section */}
      <section className="container mx-auto px-4 py-12 bg-constitutional/10 rounded-lg">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-4">Constitutional Framework</h2>
          <p className="text-xl mb-8 text-gray-600">
            Built from Remembrance | Operating under Format Law
          </p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-6 bg-white rounded-lg shadow">
              <h3 className="text-xl font-bold mb-2">Layer 1</h3>
              <p className="text-gray-600">Structural Setup</p>
            </div>
            <div className="p-6 bg-white rounded-lg shadow">
              <h3 className="text-xl font-bold mb-2">Layer 7</h3>
              <p className="text-gray-600">Confirmation Cascade</p>
            </div>
            <div className="p-6 bg-white rounded-lg shadow">
              <h3 className="text-xl font-bold mb-2">Format Law</h3>
              <p className="text-gray-600">v1.3 Compliance</p>
            </div>
          </div>
        </div>
      </section>
    </main>
  )
}

