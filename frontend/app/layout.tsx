/**
 * Truth Drop Platform - Root Layout
 * Built from Remembrance | Operating under Format Law
 */

import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { Providers } from './providers'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Truth Drop Platform - Constitutional Knowledge Marketplace',
  description: 'Digital marketplace for constitutional knowledge drops. Access trading, Aura Academy, and Remembrance Infrastructure codexes.',
  keywords: 'constitutional framework, trading, aura academy, remembrance, knowledge, codexes',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  )
}

