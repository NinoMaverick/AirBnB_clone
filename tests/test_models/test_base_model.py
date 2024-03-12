#!/usr/bin/python3
"""
unittest for BaseModel Class
"""

def test_to_dict(self):
    """send to dict"""
    base = BaseModel()
    base.name = "labrat"
    base.age = 25
    dic = base.to_dict()
    self.assertEqual(dic["id"], rat.id)
    self.assertEqual(dic["__class__"], type(base).__name__)
    self.assertEqual(dic["created_at"], base.created_at.isoformat())
    self.assertEqual(dic["updated_at"], base.updated_at.isoformat())
    self.assertEqual(dic["name"], base.name)
    self.assertEqual(dic["age"], base.age)

if __name__ == '__main__':
    unittest.main()