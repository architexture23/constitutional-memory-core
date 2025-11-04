/**
 * Truth Drop Platform - TypeScript Types
 * Built from Remembrance | Operating under Format Law
 */

export interface Codex {
  id: number
  title: string
  slug: string
  description?: string
  content?: string
  domain?: Domain
  tags?: Tag[]
  price?: number
  currency: string
  format_law_version: string
  constitutional_compliance: boolean
  remembrance_integration: boolean
  version: string
  is_active: boolean
  is_featured: boolean
  view_count: number
  purchase_count: number
  download_count: number
  created_at: string
  updated_at?: string
  published_at?: string
}

export interface Domain {
  id: number
  name: string
  slug: string
  description?: string
  icon?: string
  color?: string
  is_active: boolean
  sort_order: number
  created_at: string
  updated_at?: string
}

export interface Tag {
  id: number
  name: string
  slug: string
  description?: string
  color?: string
  created_at: string
}

export interface User {
  id: number
  email: string
  username: string
  full_name?: string
  is_active: boolean
  is_admin: boolean
  is_verified: boolean
  subscription_type?: string
  subscription_expires_at?: string
  created_at: string
  updated_at?: string
  last_login?: string
}

export interface Purchase {
  id: number
  user_id: number
  codex_id?: number
  amount: number
  currency: string
  purchase_type: 'individual' | 'bundle' | 'subscription'
  stripe_payment_intent_id?: string
  stripe_charge_id?: string
  payment_status: 'pending' | 'completed' | 'failed'
  created_at: string
  completed_at?: string
  codex?: Codex
}

