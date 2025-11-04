-- Truth Drop Platform - Initial Database Schema
-- Built from Remembrance | Operating under Format Law
-- Constitutional Framework: Layer 1 - Structural Setup

-- Domains table
CREATE TABLE IF NOT EXISTS domains (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    icon VARCHAR(255),
    color VARCHAR(7),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    sort_order INTEGER DEFAULT 0 NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_domains_name ON domains(name);
CREATE INDEX idx_domains_slug ON domains(slug);
CREATE INDEX idx_domains_active ON domains(is_active);

-- Tags table
CREATE TABLE IF NOT EXISTS tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    slug VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    color VARCHAR(7),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tags_name ON tags(name);
CREATE INDEX idx_tags_slug ON tags(slug);

-- Codexes table
CREATE TABLE IF NOT EXISTS codexes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    content TEXT,
    domain_id INTEGER REFERENCES domains(id),
    price FLOAT,
    currency VARCHAR(3) DEFAULT 'USD' NOT NULL,
    file_path VARCHAR(500),
    pdf_path VARCHAR(500),
    epub_path VARCHAR(500),
    format_law_version VARCHAR(10) DEFAULT 'v1.3' NOT NULL,
    constitutional_compliance BOOLEAN DEFAULT TRUE NOT NULL,
    remembrance_integration BOOLEAN DEFAULT TRUE NOT NULL,
    version VARCHAR(20) DEFAULT '1.0.0' NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_featured BOOLEAN DEFAULT FALSE NOT NULL,
    view_count INTEGER DEFAULT 0 NOT NULL,
    purchase_count INTEGER DEFAULT 0 NOT NULL,
    download_count INTEGER DEFAULT 0 NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    published_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_codexes_title ON codexes(title);
CREATE INDEX idx_codexes_slug ON codexes(slug);
CREATE INDEX idx_codexes_domain ON codexes(domain_id);
CREATE INDEX idx_codexes_active ON codexes(is_active);
CREATE INDEX idx_codexes_featured ON codexes(is_featured);

-- Codex-Tag association table
CREATE TABLE IF NOT EXISTS codex_tag_association (
    codex_id INTEGER REFERENCES codexes(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (codex_id, tag_id)
);

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE NOT NULL,
    subscription_type VARCHAR(50),
    subscription_expires_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    last_login TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_active ON users(is_active);

-- Purchases table
CREATE TABLE IF NOT EXISTS purchases (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) NOT NULL,
    codex_id INTEGER REFERENCES codexes(id),
    amount FLOAT NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD' NOT NULL,
    stripe_payment_intent_id VARCHAR(255),
    stripe_charge_id VARCHAR(255),
    payment_status VARCHAR(50) DEFAULT 'pending' NOT NULL,
    purchase_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_purchases_user ON purchases(user_id);
CREATE INDEX idx_purchases_codex ON purchases(codex_id);
CREATE INDEX idx_purchases_payment_intent ON purchases(stripe_payment_intent_id);
CREATE INDEX idx_purchases_status ON purchases(payment_status);

-- Bundles table (for future use)
CREATE TABLE IF NOT EXISTS bundles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD' NOT NULL,
    discount_percentage FLOAT,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_bundles_name ON bundles(name);
CREATE INDEX idx_bundles_slug ON bundles(slug);
CREATE INDEX idx_bundles_active ON bundles(is_active);

-- Insert default domains
INSERT INTO domains (name, slug, description, icon, color, sort_order) VALUES
('Trading', 'trading', 'Constitutional trading framework', '💹', '#00AA00', 1),
('Aura Academy', 'aura-academy', 'Recognition through remembrance game', '🎮', '#9B59B6', 2),
('Remembrance Infrastructure', 'remembrance-infrastructure', 'Constitutional knowledge structure', '📚', '#3498DB', 3)
ON CONFLICT (slug) DO NOTHING;

