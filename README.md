# discrete-math

lad for discrete math

## Task 1

> [!info] Input:
> n.

> [!info] Output:
> A sequence of permutations of the set {1,...,n}, where each subsequent permutation is formed from the previous one by performing a single transposition.

```pseudo code
Procedure B(m, i);
begin
    if (m mod 2 = 0) and (m > 2) then
        if i < m - 1 then B := i
        else B := m - 2
    else B := m - 1
end; (*B*)

Procedure PERM(m); (array P is global)
begin
    if m = 1 then (P[1],...,P[m] form a new permutation)
        write (P[1],...,P[n])
    else
        for i := 1 to m do
            begin PERM(m - 1);
                if i < m then P[B(m, i)] :=: P[m]
            end
end; (*PERM*)

begin (main program)
    for i := 1 to n do P[i] := i;
    PERM(n)
end
```

## Task 2

> [!info] Input:
> n.

> [!info] Output:
> The sequence of all partitions of the set {1,...,n}, where each subsequent partition is formed from the previous one by moving a single element to a different block.

```pseudo code
begin
   for i := 1 to n do (* place i in the first block *)
   begin
      BLOCK[i] := 1;
      FORWARD[i] := true;
   end;

   NEXT[1] := 0;
   output the partition;

   j := n; (* j = active element *)
   while j > 1 do
   begin
      k := BLOCK[j];
      
      if FORWARD[j] then (* j moves forward *)
      begin
         if NEXT[k] = 0 then (* k is the last block *)
         begin
            NEXT[k] := j;
            PREV[j] := k;
            NEXT[j] := 0;
         end;
         
         if NEXT[k] > j then (* j forms a new block *)
         begin
            PREV[j] := k;
            NEXT[j] := NEXT[k];
            PREV[NEXT[j]] := j;
            NEXT[k] := j;
         end;
         
         BLOCK[j] := NEXT[k];
      end
      else (* j moves backward *)
      begin
         BLOCK[j] := PREV[k];
         
         if k = j then (* j forms a singleton block *)
         begin
            if NEXT[k] = 0 then
               NEXT[PREV[k]] := 0;
            else
            begin
               NEXT[PREV[k]] := NEXT[k];
               PREV[NEXT[k]] := PREV[k];
            end;
         end;
      end;
      
      output the partition;
      
      j := n;
      while (j > 1) and ((FORWARD[j] and (BLOCK[j] = j)) or (not FORWARD[j] and (BLOCK[j] = 1))) do
      begin
         FORWARD[j] := not FORWARD[j];
         j := j - 1;
      end;
   end;
end
```