import { PrismaClient } from '@prisma/client';
import { userData } from './seedData';

const prisma = new PrismaClient();

async function main() {
  for (const user of userData) {
    await prisma.user.create({
      data: user,
    });
  }

  console.log('Seeding completed.');
}

main()
  .catch(async (e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
