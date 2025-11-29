# Data Model

This agent operates on simple numerical inputs and outputs. There is no complex data model or persistent storage required.

## Entities

*   **Number**: Represents an input operand for `add` or `subtract` functions.
    *   **Type**: Float (to accommodate both integers and decimal values).
    *   **Constraints**: Must be a valid numerical value.
*   **Result**: Represents the output of `add` or `subtract` functions.
    *   **Type**: Float.

## Relationships

N/A - The operations are stateless and do not involve relationships between entities.

## Validation Rules

*   All inputs to `add` and `subtract` functions must be of type `Number`. Non-numeric inputs will result in an error.
