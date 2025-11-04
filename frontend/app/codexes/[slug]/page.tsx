/**
 * Truth Drop Platform - Codex Detail Page
 * Built from Remembrance | Operating under Format Law
 */

'use client'

import { useState, useEffect, use } from 'react'
import { codexApi } from '@/lib/api'
import Link from 'next/link'
import { notFound } from 'next/navigation'

export default function CodexDetailPage({ params }: { params: Promise<{ slug: string }> | { slug: string } }) {
  // Handle both Promise and direct params (Next.js 14 compatibility)
  const resolvedParams = params instanceof Promise ? use(params) : params
  const slug = resolvedParams.slug
  const [codex, setCodex] = useState<any>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isPurchasing, setIsPurchasing] = useState(false)

  const handlePurchase = async () => {
    if (!codex || !codex.id || isPurchasing) return
    
    setIsPurchasing(true)
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/purchases/create-checkout-session`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ codex_id: codex.id }),
      })

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ detail: 'Failed to create checkout session' }))
        throw new Error(errorData.detail || 'Failed to create checkout session')
      }

      const data = await response.json()
      if (data.checkout_url) {
        // Redirect to Stripe Checkout
        window.location.href = data.checkout_url
      } else {
        throw new Error('No checkout URL received')
      }
    } catch (err: any) {
      console.error('Purchase error:', err)
      let errorMessage = 'Unknown error'
      
      // Extract error message from various error formats
      if (err instanceof Error) {
        errorMessage = err.message
      } else if (err?.message) {
        errorMessage = err.message
      } else if (typeof err === 'string') {
        errorMessage = err
      } else if (err?.detail) {
        errorMessage = err.detail
      } else if (err?.error) {
        errorMessage = err.error
      } else if (err?.response?.data?.detail) {
        errorMessage = err.response.data.detail
      } else {
        errorMessage = JSON.stringify(err) || 'Unknown error'
      }
      
      alert(`Purchase failed: ${errorMessage}`)
      setIsPurchasing(false)
    }
  }

  useEffect(() => {
    loadCodex()
  }, [slug])

  const loadCodex = async () => {
    setIsLoading(true)
    try {
      // Get all codexes and find by slug (until we have a slug endpoint)
      const response = await codexApi.list()
      const codexes = Array.isArray(response.data) ? response.data : []
      const found = codexes.find((c: any) => c.slug === slug)
      
      if (found) {
        setCodex(found)
      } else {
        notFound()
      }
    } catch (error) {
      console.error('Error loading codex:', error)
      notFound()
    } finally {
      setIsLoading(false)
    }
  }

  if (isLoading) {
    return (
      <main className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
        <div>Loading codex...</div>
      </main>
    )
  }

  if (!codex) {
    notFound()
    return null
  }

  return (
    <main className="min-h-screen bg-gray-900 text-white">
      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <Link href="/" className="text-constitutional hover:text-constitutional-dark">
            ← Back to Home
          </Link>
        </div>
        
        <article className="max-w-4xl mx-auto">
          <h1 className="text-4xl font-bold mb-4">{codex.title}</h1>
          
          {codex.domain && (
            <div className="mb-4">
              <span className="px-3 py-1 bg-constitutional/20 text-constitutional rounded-full">
                {codex.domain.name}
              </span>
            </div>
          )}
          
          {codex.description && (
            <p className="text-xl text-gray-300 mb-6">{codex.description}</p>
          )}
          
          {codex.price !== null && (
            <div className="mb-6">
              <span className="text-3xl font-bold">${codex.price.toFixed(2)}</span>
              <span className="text-gray-400 ml-2">{codex.currency}</span>
            </div>
          )}

          {codex.price !== null && codex.price > 0 && (
            <div className="mb-8">
              <button
                onClick={handlePurchase}
                disabled={isPurchasing}
                className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-bold py-3 px-8 rounded-lg transition duration-300 ease-in-out transform hover:scale-105"
              >
                {isPurchasing ? 'Processing...' : 'Purchase Now'}
              </button>
            </div>
          )}

          {codex.price !== null && codex.price === 0 && (
            <div className="mb-8">
              <button
                onClick={handlePurchase}
                disabled={isPurchasing}
                className="bg-green-600 hover:bg-green-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-bold py-3 px-8 rounded-lg transition duration-300 ease-in-out transform hover:scale-105"
              >
                {isPurchasing ? 'Processing...' : 'Get Free'}
              </button>
            </div>
          )}
          
          {codex.content && (
            <div className="prose prose-invert max-w-none">
              <pre className="whitespace-pre-wrap bg-gray-800 p-6 rounded-lg">
                {codex.content}
              </pre>
            </div>
          )}
        </article>
      </div>
    </main>
  )
}

