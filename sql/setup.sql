DROP DATABASE IF EXISTS db_test_python_script;
CREATE DATABASE IF NOT EXISTS db_test_python_script;
USE db_test_python_script;

CREATE TABLE IF NOT EXISTS Alunos
(
    id   INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela para armazenar informações sobre as disciplinas
CREATE TABLE IF NOT EXISTS Disciplinas
(
    id   INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela para armazenar notas dos alunos nas disciplinas
CREATE TABLE IF NOT EXISTS Notas
(
    nota_id       INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id      INT,
    disciplina_id INT,
    nota          DECIMAL(4, 2),
    FOREIGN KEY (aluno_id) REFERENCES Alunos (id),
    FOREIGN KEY (disciplina_id) REFERENCES Disciplinas (id)
);

SELECT * FROM Alunos;
SELECT * FROM Disciplinas;
SELECT * FROM Notas;

-- 4. Consultas para verificar quais alunos foram aprovados, reprovados ou estão de exame
-- Alunos aprovados (nota acima de 7 em todas as disciplinas)
SELECT A.nome AS aluno, D.nome AS disciplina, N.nota
FROM Alunos A
         JOIN Notas N ON A.id = N.aluno_id
         JOIN Disciplinas D ON N.disciplina_id = D.id
WHERE N.nota > 7;

-- Alunos reprovados (nota abaixo de 5 em qualquer disciplina)
SELECT A.nome AS aluno, D.nome AS disciplina, N.nota
FROM Alunos A
         JOIN Notas N ON A.id = N.aluno_id
         JOIN Disciplinas D ON N.disciplina_id = D.id
WHERE N.nota < 5;

-- Alunos em exame (nota entre 5 e 7 em qualquer disciplina)
SELECT A.nome AS aluno, D.nome AS disciplina, N.nota
FROM Alunos A
         JOIN Notas N ON A.id = N.aluno_id
         JOIN Disciplinas D ON N.disciplina_id = D.id
WHERE N.nota BETWEEN 5 AND 7;

-- 5. Consulta para mostrar a nota máxima, mínima e média de cada aluno
SELECT A.nome      AS aluno,
       MAX(N.nota) AS nota_maxima,
       MIN(N.nota) AS nota_minima,
       AVG(N.nota) AS nota_media
FROM Alunos A
         JOIN Notas N ON A.id = N.aluno_id
GROUP BY A.nome;


/*
1 - Crie uma base de dados pensando em uma escola de pequeno porte com no máximo 5 tabelas
 , insira dados a estas tabelas e faças consultas para saber quais alunos foram aprovados, quais foram reprovas e quantos estão de exame
 Alunos que obtiverem nota acima de 7 aprovados, abaixo de 5 reprovados, entre 5 e 7 de exame

 2 - Crie uma consulta que mostre a nota máxima, mínima e média de cada aluno
 */