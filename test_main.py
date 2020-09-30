import main

def test_correct(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('F :- ((kak  ,kakat) , lol).\nF.\ng :- pc , eew;(fw).')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Correct syntax\n'

def test_correct_from_condition(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('f.\n f :- g.\nf :- g, h; t.\nf :- g, (h; t).')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Correct syntax\n'

def test_correct_long_expression(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('this :- (lorem , (ipsum ; how) , (to ; get) , (wow) ; scopes , no , (no ; now)).\nf.')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Correct syntax\n'

def test_incorrect_without_dot(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('f.\n f')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 2, colon 2\n'

def test_incorrect_without_dot_with_scope(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('f :- (w)\nf.')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 2, colon 0\n'

def test_incorrect_without_dot_one_line(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('f :- (w)')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 1, colon 8\n'

def test_incorrect_head(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('f.\n dwwd :- wef. \n :- f ; e')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 3, colon 1\n'

def test_incorrect_body(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('foo :- .\n dwwd :- wef. \n t :- f ; e')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 1, colon 7\n'

def test_incorrect_conj(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('foo :- kek ; lol.\ndwwd :- def ; wef , . \n t :- f ; e')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 2, colon 20\n'

def test_incorrect_disj(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('foo :- kek ; lol.\ndwwd :- def ; few , . \n t :- f ; e')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 2, colon 20\n'

def test_incorrect_scopes1(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('foo :- kek ; lol.\ndwwd :- def ; few,fwe . \n t :- (f ; e) , ew).')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 3, colon 18\n'

def test_incorrect_scopes2(tmp_path, monkeypatch, capsys):
    (tmp_path / 'a.txt').write_text('foo :- kek ; lol.\ndwwd :- def ; few,fwe . \nt :- h, (ew)) .\nf.')
    monkeypatch.chdir(tmp_path)
    main.main(['a.txt'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Syntax error: line 3, colon 12\n'
