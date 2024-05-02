import NextAuth from 'next-auth';
import { authConfig } from './auth.config';
import Credentials from 'next-auth/providers/credentials';
import { z } from 'zod';

export const { auth, signIn, signOut } = NextAuth({
  ...authConfig,
  providers: [
    Credentials({
      async authorize(credentials) {
        const parsdCredentials = z
          .object({
            email: z.string().email(),
            password: z.string().min(6),
          })
          .safeParse(credentials);
        if (!parsdCredentials.success) {
          throw new Error('Invalid credentials');
        }

        // sample user
        const sampleUser = {
          id: '1',
          name: 'John Doe',
          email: 'john@example.com',
          password: 'password123',
        };

        if (
          parsdCredentials.data.email === sampleUser.email &&
          parsdCredentials.data.password === sampleUser.password
        ) {
          return sampleUser;
        }

        return null;
      },
    }),
  ],
});
