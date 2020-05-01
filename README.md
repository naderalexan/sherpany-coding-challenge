# SHERPANY task

### Basic Event management API

#### RUN
- `docker-compose up --build`
- Go to `localhost`

#### Docs
Open api spec in yaml format at docs.yaml. Can be viewed through [editor.swagger.io](https://editor.swagger.io/)

#### Notes
> Assume there will be many thousands of events, users and participants per event.

This signifies that the many-to-many relationship of events to participants can be in the millions and thus a `COUNT (*)` can be rather expensive, and although caching is a good solution, maintaining the count as a separate field has higher performance and removes the need for handling cache invalidation logic. 