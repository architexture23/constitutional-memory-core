/**
 * Truth Drop Platform - Hero Component
 * Built from Remembrance | Operating under Format Law
 */

'use client'

import Link from 'next/link'

export function Hero() {
  return (
    <section className="bg-gradient-to-r from-constitutional to-remembrance text-white py-20">
      <div className="container mx-auto px-4 text-center">
        <h1 className="text-6xl font-bold mb-6">
          Truth Drop Platform
        </h1>
        <p className="text-2xl mb-8 max-w-3xl mx-auto">
          Digital marketplace for constitutional knowledge drops.
          Built from Remembrance. Operating under Format Law.
        </p>
        <div className="flex gap-4 justify-center">
          <Link
            href="/codexes"
            className="px-8 py-3 bg-white text-constitutional rounded-lg font-semibold hover:bg-gray-100 transition"
          >
            Browse Codexes
          </Link>
          <Link
            href="/search"
            className="px-8 py-3 bg-transparent border-2 border-white text-white rounded-lg font-semibold hover:bg-white/10 transition"
          >
            Search Knowledge
          </Link>
        </div>
        <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
          <div className="p-6 bg-white/10 rounded-lg backdrop-blur">
            <h3 className="text-xl font-bold mb-2">Trading</h3>
            <p className="text-sm">97+ constitutional trading documents</p>
          </div>
          <div className="p-6 bg-white/10 rounded-lg backdrop-blur">
            <h3 className="text-xl font-bold mb-2">Aura Academy</h3>
            <p className="text-sm">Recognition through remembrance</p>
          </div>
          <div className="p-6 bg-white/10 rounded-lg backdrop-blur">
            <h3 className="text-xl font-bold mb-2">Remembrance</h3>
            <p className="text-sm">738+ files of constitutional structure</p>
          </div>
        </div>
      </div>
    </section>
  )
}

