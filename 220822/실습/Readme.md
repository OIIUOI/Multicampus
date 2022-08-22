### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.

| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT * FROM playlist_track AS A 
ORDER BY playlistid DESC LIMIT 5;
```

PlaylistId  TrackId

----------  -------

18          597
17          3290
17          2096
17          2095
17          2094

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요

| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT * FROM tracks AS B 
ORDER BY TrackId LIMIT 5;
```

for those about to rock
balls to the wall
fast as a shark
restless and wild
princess of the dawn

### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.

| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 

```sql
SELECT playlistId, Name
FROM Playlist_track
INNER JOIN tracks
ON playlist_track.trackId = tracks.trackId
ORDER BY playlistId DESC LIMIT 10;
```
PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls


### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요.

| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT playlistID, name FROM tracks 
LEFT JOIN playlist_track 
ON tracks.TrackId = playlist_track.trackID
WHERE playlistID = 10 ORDER BY name DESC LIMIT 5;
```

PlaylistId  Name

----------  ------------------------

10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.

```sql
SELECT count(*) FROM tracks 
INNER JOIN artists
  ON tracks.composer = artists.name;
```

402

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.

```sql
SELECT count(*) FROM tracks
LEFT JOIN artists
ON tracks.composer = artists.name;
```

3503

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.

INNER JOIN 은 composer행에서 1명의 가수만 있어야 artist 테이블에서 매칭되면서 (=교집합이 되면서) 수가 세어지고, 
LEFT JOIN 은 composer행에서 2명의 가수가 있을 경우에도 수가 세어지기 때문에(=교집합이 아닌 경우에도) 수가 차이가 난다

### 8. invoice_items 테이블의 데이터를 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT invoicelineid, invoiceid FROM invoice_items
ORDER BY invoiceid LIMIT 5;
```

InvoiceLineId  InvoiceId

-------------  ---------

1              1
2              1
3              2
4              2
5              2

### 9. invoices 테이블의 데이터를 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT invoiceid, customerid FROM invoices
ORDER BY invoiceid LIMIT 5;
```
InvoiceId  CustomerId
---------  ----------

1          2
2          4
3          8
4          14
5          23

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.? 

```sql
SELECT InvoiceLineId, invoice_items.invoiceId
FROM invoice_items INNER JOIN invoices
ON invoice_items.invoiceId = invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC LIMIT 5;
```
InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2226           411
2227           411
2228           411
2229           411

### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
SELECT A.InvoiceId, A.CustomerId
FROM invoices AS A
INNER JOIN customers AS B
ON A.CustomerId = B.CustomerId
ORDER BY InvoiceId DESC LIMIT 5;
```

InvoiceId  CustomerId

---------  ----------

412        58
411        44
410        35
409        29
408        25

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
SELECT Ii.InvoiceLineId, Ii.invoiceId, Ct.customerId
FROM invoice_items AS Ii
INNER JOIN invoices AS Iv
ON Ii.InvoiceId = Iv.InvoiceId
INNER JOIN customers AS Ct
ON Iv.customerId = Ct.CustomerId
ORDER BY Ii.invoiceId DESC LIMIT 5;
```

InvoiceLineId  InvoiceId  CustomerId

-------------  ---------  ----------

2240           412        58
2239           411        44
2238           411        44
2237           411        44
2236           411        44

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.

| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT invoices.customerId, count(*)
FROM invoice_items
LEFT JOIN invoices
ON invoice_items.invoiceID = invoices.InvoiceId
GROUP BY invoices.customerId
ORDER BY customerId LIMIT 5;
```

CustomerId  count(*)

----------  --------

1           38
2           38
3           38
4           38
5           38
