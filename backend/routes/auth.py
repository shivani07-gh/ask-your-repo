from fastapi import APIRouter, HTTPException

from backend.database.mongodb import users_collection

from backend.schemas.user_schema import (
    UserCreate,
    UserLogin
)

from backend.utils.hashing import (
    hash_password,
    verify_password
)

from backend.utils.jwt_handler import (
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =====================
# SIGNUP
# =====================

@router.post("/signup")
async def signup(user: UserCreate):

    existing_user = await users_collection.find_one(
        {
            "email": user.email
        }
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hash_password(user.password)
    }

    await users_collection.insert_one(new_user)

    return {
        "message": "User registered successfully 🚀"
    }


# =====================
# LOGIN
# =====================

@router.post("/login")
async def login(user: UserLogin):

    db_user = await users_collection.find_one(
        {
            "email": user.email
        }
    )

    print("USER FROM DB:", db_user)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    if not verify_password(
        user.password,
        db_user["password"]
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    token = create_access_token(
        {
            "sub": user.email
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }