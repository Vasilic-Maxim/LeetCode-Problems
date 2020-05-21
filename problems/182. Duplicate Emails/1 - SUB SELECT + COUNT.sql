SELECT DISTINCT Email
FROM Person AS P1
WHERE (
    SELECT COUNT(P2.Email)
    FROM Person AS P2
    WHERE P1.Email = P2.Email
) > 1