'use client'

/**
 * Truth Drop Platform - Purchase Success Page
 * Built from Remembrance | Operating under Format Law
 */

import Link from 'next/link'
import { useSearchParams } from 'next/navigation'
import { useEffect, useState, Suspense } from 'react'

function PurchaseSuccessContent() {
  const searchParams = useSearchParams()
  const sessionId = searchParams.get('session_id')
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    // Optional: Verify purchase with backend using session_id
    if (sessionId) {
      // You can add backend verification here later
      setIsLoading(false)
    } else {
      setIsLoading(false)
    }
  }, [sessionId])

  if (isLoading) {
    return (
      <main className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p>Verifying purchase...</p>
        </div>
      </main>
    )
  }

  return (
    <main className="min-h-screen bg-gray-900 text-white flex items-center justify-center p-4">
      <div className="bg-gray-800 p-8 rounded-lg shadow-xl text-center max-w-md w-full">
        <div className="mb-6">
          <div className="mx-auto w-16 h-16 bg-green-500 rounded-full flex items-center justify-center mb-4">
            <svg className="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h1 className="text-4xl font-bold text-green-400 mb-4">Purchase Successful!</h1>
          <p className="text-lg mb-6">
            Thank you for your purchase. Your constitutional knowledge is now accessible.
          </p>
          {sessionId && (
            <p className="text-sm text-gray-400 mb-6">
              Transaction ID: {sessionId.substring(0, 20)}...
            </p>
          )}
        </div>
        
        <div className="space-y-4">
          <Link 
            href="/codexes" 
            className="block bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition duration-300 ease-in-out transform hover:scale-105"
          >
            Browse More Codexes
          </Link>
          <Link 
            href="/" 
            className="block bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-6 rounded-lg transition duration-300 ease-in-out"
          >
            Return to Homepage
          </Link>
        </div>

        <p className="text-sm text-gray-400 mt-6">
          A receipt has been sent to your email. Access to your purchased content will be available shortly.
        </p>
      </div>
    </main>
  )
}

export default function PurchaseSuccessPage() {
  return (
    <Suspense fallback={
      <main className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p>Loading...</p>
        </div>
      </main>
    }>
      <PurchaseSuccessContent />
    </Suspense>
  )
}

