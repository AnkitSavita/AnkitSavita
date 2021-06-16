/*

Cleaning Data in SQL Queries

*/


SELECT *
FROM [Alex Analyst]..[Nashville Housing]

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Standardize Date Format


SELECT SaleDate
FROM [Alex Analyst]..[Nashville Housing]

SELECT SaleDate, CONVERT(DATE, SaleDate)
FROM [Alex Analyst]..[Nashville Housing]

ALTER TABLE [Nashville Housing]
ADD SaleDateConverted DATE;

UPDATE [Nashville Housing]
SET SaleDateConverted = CONVERT(DATE, SaleDate)

SELECT SaleDate, SaleDateConverted
FROM [Alex Analyst]..[Nashville Housing]

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


--Populate Property Address data


SELECT PropertyAddress
FROM [Alex Analyst]..[Nashville Housing]


SELECT PropertyAddress
FROM [Alex Analyst]..[Nashville Housing]
WHERE PropertyAddress IS NULL


SELECT *
FROM [Alex Analyst]..[Nashville Housing]
WHERE PropertyAddress IS NULL


SELECT *
FROM [Alex Analyst]..[Nashville Housing]
ORDER BY ParcelID


SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress
FROM [Alex Analyst]..[Nashville Housing] AS a
JOIN [Alex Analyst]..[Nashville Housing] AS b
    ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress IS NULL


SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM [Alex Analyst]..[Nashville Housing] AS a
JOIN [Alex Analyst]..[Nashville Housing] AS b
    ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress IS NULL


UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM [Alex Analyst]..[Nashville Housing] AS a
JOIN [Alex Analyst]..[Nashville Housing] AS b
    ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress IS NULL

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-- Breaking out Address into Individual Columns (Address, City, State)


SELECT PropertyAddress
FROM [Alex Analyst]..[Nashville Housing]


SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)) AS Address
FROM [Alex Analyst]..[Nashville Housing]


SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) AS Address
FROM [Alex Analyst]..[Nashville Housing]


SELECT
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress)) AS City
FROM [Alex Analyst]..[Nashville Housing]


ALTER TABLE [Nashville Housing]
ADD PropertySplitAddress NVARCHAR(255);

UPDATE [Nashville Housing]
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)



ALTER TABLE [Nashville Housing]
ADD PropertySplitCity NVARCHAR(255);

UPDATE [Nashville Housing]
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress))


SELECT *
FROM [Alex Analyst]..[Nashville Housing]


SELECT OwnerAddress
FROM [Alex Analyst]..[Nashville Housing]


SELECT
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3),
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2),
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
FROM [Alex Analyst]..[Nashville Housing]



ALTER TABLE [Nashville Housing]
ADD OwnerSplitAddress NVARCHAR(255);

UPDATE [Nashville Housing]
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)


ALTER TABLE [Nashville Housing]
ADD OwnerSplitCity NVARCHAR(255);

UPDATE [Nashville Housing]
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)


ALTER TABLE [Nashville Housing]
ADD OwnerSplitState NVARCHAR(255);

UPDATE [Nashville Housing]
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)


SELECT *
FROM [Alex Analyst]..[Nashville Housing]


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-- Change Y and N to Yes and No in "Sold As Vacant" firld


SELECT DISTINCT(SoldAsVacant)
FROM [Alex Analyst]..[Nashville Housing]


SELECT DISTINCT(SoldAsVacant), COUNT(SoldAsVacant)
FROM [Alex Analyst]..[Nashville Housing]
GROUP BY SoldAsVacant
ORDER BY 2


SELECT SoldAsVacant
, CASE WHEN SoldAsVacant = 'Y' THEN 'YES'
	   WHEN SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END
FROM [Alex Analyst]..[Nashville Housing]


UPDATE [Nashville Housing]
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'YES'
	   WHEN SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-- Remove duplicates


WITH RowNumCTE AS(
SELECT *,
     ROW_NUMBER() OVER (
	 PARTITION BY ParcelID,
	              PropertyAddress,
				  SalePrice,
				  SaleDate,
				  LegalReference
				  ORDER BY
				       UniqueID
					   ) row_num

FROM [Alex Analyst]..[Nashville Housing]
)

SELECT *
FROM RowNumCTE
WHERE row_num > 1
ORDER BY PropertyAddress


WITH RowNumCTE AS(
SELECT *,
     ROW_NUMBER() OVER (
	 PARTITION BY ParcelID,
	              PropertyAddress,
				  SalePrice,
				  SaleDate,
				  LegalReference
				  ORDER BY
				       UniqueID
					   ) row_num

FROM [Alex Analyst]..[Nashville Housing]
)

DELETE
FROM RowNumCTE
WHERE row_num > 1



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-- Delete Unused Columns


SELECT *
FROM [Alex Analyst]..[Nashville Housing]


ALTER TABLE [Alex Analyst]..[Nashville Housing]
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress


ALTER TABLE [Alex Analyst]..[Nashville Housing]
DROP COLUMN SaleDate




















