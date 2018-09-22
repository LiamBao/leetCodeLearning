def prints(s):
    for i in s:
        print(str(s))

class Solution(object):
    def parse_idx(self, nums, target):
        data = {}
        for idx,num in enumerate(nums):
            if num in data:
                return [idx,data[num]] 
            else:
                data[target-num] = idx
        return data

s = [1,2,4,23,2,32,23,23,23,23,34,43,42,123,54,4545]
print(str(Solution().parse_idx(s, 27)))


class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    followed = db.relationship('Follow',
                               foreign_keys=[Follow.follower_id])
    followers = db.relationship('Follow',
                                foreign_keys=[Follow.followed_id])

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


cat testdata | sort | uniq -c | sort -k1,1nr | head -10
cat testdata | awk '{print $2}' | sort | uniq -c | sort -n -r | head -n 1
grep requestKey log4j.log|awk '{print $2}'|sort|uniq -c|sort -k1nr|head -10
cut -d "|" -f 1 | sort | uniq -c | sort -k1nr | head -10