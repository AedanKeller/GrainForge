# The Grain Smith - Sourdough Starter E-commerce Platform

## Overview

The Grain Smith is a Flask-based e-commerce web application that sells plastic-free sourdough starter kits. The application features a product showcase homepage, checkout functionality, and order management system with an eco-friendly, autumn-inspired design theme.

## User Preferences

Preferred communication style: Simple, everyday language.
Design aesthetic: Premium, professional look inspired by June Home Supply - clean, sophisticated, avoiding "cheap" elements.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5 for responsive design
- **Custom Styling**: Premium color palette with refined typography (Crimson Text and Playfair Display fonts) - inspired by high-end home goods aesthetics
- **JavaScript**: Vanilla JavaScript for interactive features (smooth scrolling, navbar effects, intersection observer animations)
- **Icons**: Font Awesome for visual elements (used sparingly for premium feel)

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database ORM**: Flask-SQLAlchemy with declarative base model
- **Forms**: Flask-WTF with WTForms for form handling and validation
- **Session Management**: Flask's built-in session handling with configurable secret key

### Database Design
- **Primary Database**: SQLite (development) with PostgreSQL support via environment variable
- **Connection Pooling**: Configured with pool_recycle and pool_pre_ping for reliability
- **Schema**: Single Order model with comprehensive customer and order information

## Key Components

### Models
- **Order Model**: Stores customer information (name, email, phone, address details), order details (quantity, total_amount), and order status tracking

### Forms
- **CheckoutForm**: Comprehensive form with validation for customer details including:
  - Personal information (name, email, phone)
  - Complete address fields with US state selection
  - Quantity validation (1-10 items)

### Routes
- **Homepage (/)**: Product showcase and hero section
- **Checkout (/checkout)**: Order form processing with error handling
- **About (/about)**: Company information (redirects to homepage with anchor)

### Frontend Features
- Responsive design optimized for mobile and desktop
- Smooth scrolling navigation
- Dynamic navbar styling on scroll
- Intersection observer animations
- Product gallery and video sections

## Data Flow

1. **User Journey**: Homepage → Product information → Checkout form → Order confirmation
2. **Order Processing**: Form validation → Order creation → Database storage → Success/error feedback
3. **Error Handling**: Database rollback on failures with user-friendly error messages

## External Dependencies

### Python Packages
- Flask (web framework)
- Flask-SQLAlchemy (database ORM)
- Flask-WTF (form handling)
- WTForms (form validation)

### Frontend Libraries
- Bootstrap 5 (CSS framework)
- Font Awesome (icons)
- Google Fonts (Crimson Text, Playfair Display)

### Environment Variables
- `SESSION_SECRET`: Flask session security key
- `DATABASE_URL`: Database connection string (defaults to SQLite)

## Deployment Strategy

### Development Configuration
- Debug mode enabled
- SQLite database for local development
- Host configuration for Replit deployment (0.0.0.0:5000)

### Production Considerations
- Environment-based configuration for database and secrets
- Database connection pooling for scalability
- Error logging and debugging capabilities
- Session secret management for security

### File Structure
- `app.py`: Application factory and configuration
- `main.py`: Application entry point
- `models.py`: Database models
- `routes.py`: URL routing and view functions
- `forms.py`: Form definitions and validation
- `templates/`: Jinja2 templates
- `static/`: CSS and JavaScript assets

The application follows Flask best practices with clear separation of concerns, making it easily maintainable and extensible for future e-commerce features like payment processing, inventory management, or user accounts.

## Recent Changes (July 11, 2025)

### Premium Design Upgrade
- Refined color palette from autumn-themed to sophisticated premium tones
- Removed "cheap" visual elements like excessive icons and rounded corners
- Updated typography with improved font weights and letter spacing
- Enhanced spacing and layout for a more professional appearance
- Simplified navigation labels (Gallery → Craft, About → Philosophy, Buy Now → Shop)
- Removed decorative icons from buttons and headings
- Applied June Home Supply-inspired aesthetic: clean, sophisticated, premium feel

### Microplastics Focus Update
- Emphasized zero microplastic contamination as primary value proposition
- Added dedicated microplastics education section with compelling statistics
- Updated all product messaging to highlight health protection benefits
- Repositioned brand from "plastic-free" to "microplastic-free" for stronger impact
- Enhanced checkout page with microplastic-free guarantee messaging
- Added research-backed content about plastic contamination dangers