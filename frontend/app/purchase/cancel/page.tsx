'use client'

/**
 * Truth Drop Platform - Purchase Cancel Page
 * Built from Remembrance | Operating under Format Law
 */

import Link from 'next/link'

export default function PurchaseCancelPage() {
  return (
    <main className="min-h-screen bg-gray-900 text-white flex items-center justify-center p-4">
      <div className="bg-gray-800 p-8 rounded-lg shadow-xl text-center max-w-md w-full">
        <div className="mb-6">
          <div className="mx-auto w-16 h-16 bg-yellow-500 rounded-full flex items-center justify-center mb-4">
            <svg className="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
          <h1 className="text-4xl font-bold text-yellow-400 mb-4">Purchase Canceled</h1>
          <p className="text-lg mb-6">
            Your purchase was not completed. You can try again or explore other codexes.
          </p>
        </div>
        
        <div className="space-y-4">
          <Link 
            href="/codexes" 
            className="block bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition duration-300 ease-in-out transform hover:scale-105"
          >
            Browse Codexes
          </Link>
          <Link 
            href="/" 
            className="block bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-6 rounded-lg transition duration-300 ease-in-out"
          >
            Return to Homepage
          </Link>
        </div>

        <p className="text-sm text-gray-400 mt-6">
          No charges were made to your account. Feel free to return when you're ready.
        </p>
      </div>
    </main>
  )
}

