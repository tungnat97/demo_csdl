CREATE OR REPLACE FUNCTION limit_subject_program() RETURNS TRIGGER AS $$
BEGIN
  IF (SELECT count(*) FROM employee_programsubject
	  WHERE program_id = new.program_id) = 10 THEN
    RAISE EXCEPTION 'Chương trình đào tạo đã có 10 môn học';
  END IF;
  RETURN new;
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE TRIGGER tr_limit_subject_program BEFORE INSERT ON employee_programsubject FOR EACH ROW EXECUTE PROCEDURE limit_subject_program();

CREATE OR REPLACE FUNCTION check_subject_name_program() RETURNS TRIGGER AS $$
BEGIN
  IF (SELECT count(*) FROM employee_programsubject
	 WHERE subject_id in (
		 SELECT id from employee_subject 
		 where name = (SELECT name from employee_subject where id = new.subject_id)
		 and id != new.subject_id
	 )
	 ) = 1 THEN
    RAISE EXCEPTION 'Trùng tên môn học trong chương trình đào tạo';
  END IF;
  RETURN new;
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE TRIGGER tr_check_subject_name_program BEFORE INSERT ON employee_programsubject FOR EACH ROW EXECUTE PROCEDURE check_subject_name_program();
