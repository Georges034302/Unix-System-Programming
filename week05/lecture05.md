# Lecture 05 – Regex, grep, and sed

## Data Source: file.txt

### file.txt
```
b
be
bee
beee

bad
bed
bid

go
good

12
123
1234

hat
heat

start
end
```

---

## grep commands (metacharacters)

```
grep -E 'be+' file.txt
# +  -> one or more e
# matches: be, bee, beee

grep -E 'b[aei]d' file.txt
# [] -> one character from the set
# matches: bad, bed, bid

grep -E 'be*' file.txt
# * -> zero or more e
# matches: b, be, bee, beee

grep -E '[0-9]{2}' file.txt
# {n} -> exactly 2 digits together
# matches: 12, 123, 1234

grep -E '[0-9]{2,4}' file.txt
# {m,n} -> from 2 to 4 digits
# matches: 12, 123, 1234

grep -E 'h.t' file.txt
# . -> any one character
# matches: hat

grep -E '^go' file.txt
# ^ -> start of line
# matches: go, good

grep -E 'd$' file.txt
# $ -> end of line
# matches: bad, bed, bid, good, end
```

---

## sed commands (aligned concepts)

```
sed -E 's/be+/BE/g' file.txt
# replace one or more 'e' after b → highlights +

sed -E 's/b[aei]d/BXD/g' file.txt
# replace bad/bed/bid → shows character class []

sed -E 's/be*/X/g' file.txt
# replace b, be, bee, beee → shows * (zero or more)

sed -E 's/[0-9]{2}/NUM/g' file.txt
# replace any 2-digit sequence → {n}

sed -E 's/[0-9]{2,4}/NUM/g' file.txt
# replace 2–4 digit sequences → {m,n}

sed -E 's/h.t/HIT/g' file.txt
# replace hat → shows dot (.)

sed -E 's/^go/GO/g' file.txt
# replace only if line starts with 'go' → ^

sed -E 's/d$/D/g' file.txt
# replace ending 'd' → $
```

---
