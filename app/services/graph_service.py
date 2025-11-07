import numpy as np
from sqlalchemy.orm import Session

from app.db.models import SymptomEmbedding


def add_symptom_embedding(db: Session, uid: int, symptom: str, intensity: float, embedding: list[float]):
    """
    Create and persist a 384-dimensional symptom embedding record for a user.
    
    Converts `embedding` to a flattened float32 vector, validates it has exactly 384 elements, stores it on a new SymptomEmbedding record, commits the session, refreshes the instance, and returns the persisted record.
    
    Parameters:
        uid (int): User identifier to associate with the embedding.
        symptom (str): Symptom label or name.
        intensity (float): Symptom intensity value.
        embedding (list[float] | array-like): Iterable convertible to a 384-element numeric vector.
    
    Returns:
        SymptomEmbedding: The persisted SymptomEmbedding instance refreshed from the database.
    
    Raises:
        ValueError: If the provided embedding does not contain exactly 384 elements after conversion.
        Exception: Any exception raised during database commit is rolled back and re-raised.
    """
    embedding_np = np.asarray(embedding, dtype=np.float32).ravel()
    if embedding_np.size != 384: raise ValueError("Symptom embeddings must be 384-dimensional to match storage.")
    embedding_list = embedding_np.tolist()

    record = SymptomEmbedding(
        user_hmac_id=uid,
        symptom=symptom,
        intensity=intensity,
        embedding=embedding_list
    )

    db.add(record)
    try: db.commit()
    except Exception:
        db.rollback()
        raise
    db.refresh(record)
    return record