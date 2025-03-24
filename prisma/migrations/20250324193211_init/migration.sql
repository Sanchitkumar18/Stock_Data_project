/*
  Warnings:

  - You are about to drop the column `createdAt` on the `StockData` table. All the data in the column will be lost.
  - You are about to drop the column `price` on the `StockData` table. All the data in the column will be lost.
  - You are about to drop the column `symbol` on the `StockData` table. All the data in the column will be lost.
  - A unique constraint covering the columns `[datetime]` on the table `StockData` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `close` to the `StockData` table without a default value. This is not possible if the table is not empty.
  - Added the required column `datetime` to the `StockData` table without a default value. This is not possible if the table is not empty.
  - Added the required column `high` to the `StockData` table without a default value. This is not possible if the table is not empty.
  - Added the required column `low` to the `StockData` table without a default value. This is not possible if the table is not empty.
  - Added the required column `open` to the `StockData` table without a default value. This is not possible if the table is not empty.
  - Added the required column `volume` to the `StockData` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "StockData" DROP COLUMN "createdAt",
DROP COLUMN "price",
DROP COLUMN "symbol",
ADD COLUMN     "close" DECIMAL(65,30) NOT NULL,
ADD COLUMN     "datetime" TIMESTAMP(3) NOT NULL,
ADD COLUMN     "high" DECIMAL(65,30) NOT NULL,
ADD COLUMN     "low" DECIMAL(65,30) NOT NULL,
ADD COLUMN     "open" DECIMAL(65,30) NOT NULL,
ADD COLUMN     "volume" INTEGER NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "StockData_datetime_key" ON "StockData"("datetime");
