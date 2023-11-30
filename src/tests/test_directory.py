from directory import Directory

def test_get_name(directory: Directory):
    assert directory.get_name() == 'test'

def test_to_string(directory: Directory):
   assert directory.__str__() == directory.get_name()
        
def test_get_parent(directory_with_children: Directory):
    assert directory_with_children.get_parent() == None

    for dir_name in directory_with_children.get_directories().keys():
        child_dir = directory_with_children.get_directory(dir_name)
        assert child_dir.get_parent() == directory_with_children

        for grandchild_dir in child_dir.get_directories().keys():
            grandchild_dir = child_dir.get_directory(grandchild_dir)
            assert grandchild_dir.get_parent() == child_dir

def test_depth(directory_with_children: Directory):
    assert directory_with_children.depth == 0

    for dir_name in directory_with_children.get_directories().keys():
        child_dir = directory_with_children.get_directory(dir_name)
        assert child_dir.depth == 1

        for grandchild_dir in child_dir.get_directories().keys():
            grandchild_dir = child_dir.get_directory(grandchild_dir)
            assert grandchild_dir.depth == 2

def test_set_parent(directory_with_children: Directory):
    child_dir = directory_with_children.get_directory('test')
    grandchild_dir = child_dir.get_directory('test-child')
    assert grandchild_dir.depth == 2
    assert grandchild_dir.get_parent() == child_dir
    assert grandchild_dir.path == '/test/test-child'

    grandchild_dir.set_parent(directory_with_children)
    assert grandchild_dir.depth == 1
    assert grandchild_dir.get_parent() == directory_with_children
    assert grandchild_dir.path == '/test-child'



    
