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
