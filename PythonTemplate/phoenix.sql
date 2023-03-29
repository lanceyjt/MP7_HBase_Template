DROP VIEW IF EXISTS "powers";
CREATE VIEW "powers" (pk VARCHAR PRIMARY KEY,  "personal"."hero"  VARCHAR, "personal"."power" VARCHAR, "professional"."name" VARCHAR, "professional"."xp" VARCHAR, "custom"."color" VARCHAR);
SELECT P1."name" AS "Name1", P2."name" AS "Name2", P1."power" AS "Power"
FROM "powers" AS P1
INNER JOIN "powers" as P2
ON P1."power"=P2."power"
WHERE P1."hero"='yes' and P2."hero"='yes';
