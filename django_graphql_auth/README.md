### Blog source: 
1. [Empowering Your Django Backend with GraphQL: A Powerful Combination](https://medium.com/simform-engineering/empowering-your-django-backend-with-graphql-a-powerful-combination-764babd30bb0)
2. [Empowering Your Django Backend with GraphQL: A Powerful Combination (Part — 2)](https://medium.com/simform-engineering/empowering-your-django-backend-with-graphql-a-powerful-combination-part-2-2e9b0e5f17cd)

### Queries

###### Gets all Posts 

```graphql
query getAllPost{
  posts{
    id,
    title,
    content,
    author{
      id,
      name
    }
  }
}
```

###### Creates Post by giving **title**, **content** and **authorId**
```graphql 
mutation createPost{
  createPost(authorId: 1, 
  	title:"How to win at everything",
    content:"Work Hard Bro at the right time"
  ){
    post{
      id, 
      title,
      content
    }
  }
}
```

###### Updates Post based on **id** of the post
```graphql
mutation updatePost{
  updatePost(
    id:6,
  	content: "I know you know that working hard is the ultimate way"
  ){
    post{
      id,
      title,
      content
  	}
	}
}
```

###### Deletes Post for given **id**
```graphql
mutation deletePost{
  deletePost(id:1){
    success
  }
}
```

###### Creates user based on **email**, **username** and **password**
```graphql
mutation createUser{
  createUser(email:"rbt@gmail.com", username:"rbt", password:"mypassword"){
    user{
      id,
      username,
      email
    },
    token,
    refreshToken
  }
}
```

###### Gives Token for user as **username** and **password** of the user is provided
```graphql
mutation tokenAuth{
  tokenAuth(username:"rbt", password:"shikhar111"){
    token,
    refreshToken,
    refreshExpiresIn,
    payload
  }
}
```

#### Queries With Authorization

###### Gives username based on **token** provided on Authorization header
```graphql
query whomai{
  whoami{
    username
  }
}
```
_Authorization header required for whoami. Add this json on headers_
```graphql
{
    "Authorization": "Bearer <token>"
}
```

###### Gives all users with their information 
```graphql
query allUsers{
  users{
    id,
    username,
    email,
    password
  }
}
```
_Authorization header required for allUsers. Add this json on headers_
```graphql
{
     "Authorization": "Bearer <token>"
}
```


