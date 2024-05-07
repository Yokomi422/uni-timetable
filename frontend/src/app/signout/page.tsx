'use client';

import { signOut } from 'next-auth/react';
import { useEffect } from 'react';

function SignOutPage() {
  useEffect(() => {
    signOut();
  }, []);

  return <div>Signing out...</div>;
}

export default SignOutPage;
