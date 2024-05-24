'use client';

import { config } from 'dotenv';

config();

import { supabase } from '@/utils/supabase';


import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useRouter } from 'next/navigation';
import { Box, Button, TextField } from '@mui/material';
import { z } from 'zod';

export const loginInputSchema = z.object({
  email: z
    .string()
    .email({ message: '無効なメールアドレスです' })
    .nonempty({ message: 'メールアドレスを入力してください' }),
  password: z
    .string()
    .min(6, { message: 'パスワードは6文字以上である必要があります' })
    .nonempty({ message: 'パスワードを入力してください' }),
});


export type LoginFormInput = z.infer<typeof loginInputSchema>;

const LoginPage = () => {
  const router = useRouter();
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting },
    reset,
  } = useForm<LoginFormInput>({
    resolver: zodResolver(loginInputSchema),
    defaultValues: {
      email: '',
      password: '',
    },
  });

  const onSubmit = async (input: LoginFormInput) => {
    try {
      const { email, password } = input;
      const { data,  error } = await supabase.auth.signInWithPassword({
        email,
        password,
      });

      if (error) throw new Error(error.message);
      router.push('/timetable');
    } catch (error) {
      console.error('Login error:', error);
    } finally {
      reset();
    }
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit(onSubmit)}
      sx={{ width: '100%', maxWidth: 360, mx: 'auto', mt: 8 }}
    >
      <TextField
        label="Email"
        type="email"
        variant="outlined"
        fullWidth
        margin="normal"
        {...register('email', { required: 'This field is required' })}
        error={!!errors.email}
        helperText={errors.email?.message}
      />
      <TextField
        label="Password"
        type="password"
        variant="outlined"
        fullWidth
        margin="normal"
        {...register('password', { required: 'This field is required' })}
        error={!!errors.password}
        helperText={errors.password?.message}
      />
      <Button type="submit" fullWidth variant="contained" color="primary" disabled={isSubmitting}>
        Log In
      </Button>
    </Box>
  );
};

export default LoginPage;
