/**
 * Truth Drop Platform - 404 Not Found Page
 * Built from Remembrance | Operating under Format Law
 */

import Link from 'next/link'

export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-900 text-white">
      <div className="text-center">
        <h1 className="text-6xl font-bold mb-4">404</h1>
        <h2 className="text-2xl font-semibold mb-4">This page could not be found.</h2>
        <p className="text-gray-400 mb-8">
          The page you are looking for does not exist.
        </p>
        <Link
          href="/"
          className="inline-block px-6 py-3 bg-constitutional text-white rounded-lg font-semibold hover:bg-constitutional-dark transition"
        >
          Return Home
        </Link>
      </div>
    </div>
  )
}

