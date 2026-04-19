# Notes

## HTTPx Async

Using requests works for small scale. To follow best practices, the project uses httpx async operation. this is the link for resources: https://oneuptime.com/blog/post/2026-02-03-python-httpx-async-requests/view


The transaction/sync requires a retry and sleep mechanish, that's polling + cursor handling, currently we are only getting the first cursor dta
