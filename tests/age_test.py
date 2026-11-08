import pytest
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

class TestUserProfile:
    def test_age(self):
        valid_user_path = Path(__file__).parent.parent / 'data' / 'valid' / 'input' / 'age.json'
        user = UserProfile.from_json(str(valid_user_path))
        assert user.get_age() == 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
