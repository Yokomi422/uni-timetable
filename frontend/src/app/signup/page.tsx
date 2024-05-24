"use client";

import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useRouter } from 'next/navigation';
import { Box, Button, TextField } from '@mui/material';

import { supabase } from '../../utils/supabase';
import { loginInputSchema, LoginFormInput } from '@/app/login/page';

const SignInPage = () => {
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

  const onSubmit = async (data: LoginFormInput) => {
    try {
      const { email, password } = data;
      const { data: authData, error } = await supabase.auth.signUp({
        email,
        password,
      });

      const { user, session } = authData; 

      if (error) throw new Error(error.message);
      console.log('Signed up:', user);
      router.push('/timetable');
    } catch (error) {
      console.error('Sign up error:', error);
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
        Sign Up
      </Button>
    </Box>
  );
};

export default SignInPage;

