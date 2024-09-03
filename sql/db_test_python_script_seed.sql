USE db_test_python_script;


-- Inserir dados na tabela Alunos
INSERT INTO Alunos (nome) VALUES ('Ana Silva');
INSERT INTO Alunos (nome) VALUES ('Bruno Souza');
INSERT INTO Alunos (nome) VALUES ('Carlos Lima');
INSERT INTO Alunos (nome) VALUES ('Daniela Costa');
INSERT INTO Alunos (nome) VALUES ('Elena Martins');

-- Inserir dados na tabela Disciplinas
INSERT INTO Disciplinas (nome) VALUES ('Matemática');
INSERT INTO Disciplinas (nome) VALUES ('Português');
INSERT INTO Disciplinas (nome) VALUES ('História');

-- Inserir dados na tabela Notas (Notas da Ana Silva)
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (1, 1, 8.0);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (1, 2, 7.5);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (1, 3, 9.0);

-- Inserir dados na tabela Notas (Notas do Bruno Souza)
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (2, 1, 4.0);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (2, 2, 5.5);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (2, 3, 6.0);

-- Inserir dados na tabela Notas (Notas do Carlos Lima)
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (3, 1, 6.5);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (3, 2, 7.0);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (3, 3, 5.0);

-- Inserir dados na tabela Notas (Notas da Daniela Costa)
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (4, 1, 7.5);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (4, 2, 8.0);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (4, 3, 9.0);

-- Inserir dados na tabela Notas (Notas da Elena Martins)
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (5, 1, 3.5);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (5, 2, 4.5);
INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (5, 3, 5.5);
