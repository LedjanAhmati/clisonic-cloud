/**
 * Developer Documentation Redirect
 * Redirects to the main /developers page with 37 Live Endpoints
 */

import { redirect } from 'next/navigation'

export default function DeveloperDocsRedirect() {
  redirect('/developers')
}
