# coding: utf-8

"""
    tagbase-server API

    tagbse-server provides HTTP endpoints for ingestion of various files \\ into a Tagbase SQL database. Input file support currently includes eTUFF (see [here](https://doi.org/10.6084/m9.figshare.10032848.v4) \\ and [here](https://doi.org/10.6084/m9.figshare.10159820.v1)). The REST API complies with [OpenAPI v3.0.3](https://spec.openapis.org/oas/v3.0.3.html). 

    The version of the OpenAPI document: v0.14.0
    Contact: tagtuna@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr, conbytes, constr, validator

from typing import Optional, Union

from pytagbase.models.ingest200 import Ingest200

from pytagbase.api_client import ApiClient
from pytagbase.api_response import ApiResponse
from pytagbase.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class IngestApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def ingest_get(self, file : Annotated[constr(strict=True, max_length=100, min_length=10), Field(..., description="Location of a network accessible (file, ftp, http, https) file e.g. 'file:///usr/src/app/data/eTUFF-sailfish-117259.txt'.")], notes : Annotated[Optional[constr(strict=True, max_length=10000, min_length=1)], Field(description="Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data)")] = None, type : Annotated[Optional[StrictStr], Field(description="Type of file to be ingested, defaults to 'etuff'")] = None, version : Annotated[Optional[constr(strict=True, max_length=10, min_length=1)], Field(description="Version identifier for the eTUFF tag data file ingested")] = None, **kwargs) -> Ingest200:  # noqa: E501
        """Get network accessible file and execute ingestion  # noqa: E501

        Get network accessible file and execute ingestion  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ingest_get(file, notes, type, version, async_req=True)
        >>> result = thread.get()

        :param file: Location of a network accessible (file, ftp, http, https) file e.g. 'file:///usr/src/app/data/eTUFF-sailfish-117259.txt'. (required)
        :type file: str
        :param notes: Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data)
        :type notes: str
        :param type: Type of file to be ingested, defaults to 'etuff'
        :type type: str
        :param version: Version identifier for the eTUFF tag data file ingested
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Ingest200
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the ingest_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.ingest_get_with_http_info(file, notes, type, version, **kwargs)  # noqa: E501

    @validate_arguments
    def ingest_get_with_http_info(self, file : Annotated[constr(strict=True, max_length=100, min_length=10), Field(..., description="Location of a network accessible (file, ftp, http, https) file e.g. 'file:///usr/src/app/data/eTUFF-sailfish-117259.txt'.")], notes : Annotated[Optional[constr(strict=True, max_length=10000, min_length=1)], Field(description="Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data)")] = None, type : Annotated[Optional[StrictStr], Field(description="Type of file to be ingested, defaults to 'etuff'")] = None, version : Annotated[Optional[constr(strict=True, max_length=10, min_length=1)], Field(description="Version identifier for the eTUFF tag data file ingested")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get network accessible file and execute ingestion  # noqa: E501

        Get network accessible file and execute ingestion  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ingest_get_with_http_info(file, notes, type, version, async_req=True)
        >>> result = thread.get()

        :param file: Location of a network accessible (file, ftp, http, https) file e.g. 'file:///usr/src/app/data/eTUFF-sailfish-117259.txt'. (required)
        :type file: str
        :param notes: Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data)
        :type notes: str
        :param type: Type of file to be ingested, defaults to 'etuff'
        :type type: str
        :param version: Version identifier for the eTUFF tag data file ingested
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Ingest200, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'file',
            'notes',
            'type',
            'version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ingest_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('file') is not None:  # noqa: E501
            _query_params.append(('file', _params['file']))

        if _params.get('notes') is not None:  # noqa: E501
            _query_params.append(('notes', _params['notes']))

        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Ingest200",
            '500': "ErrorContainer",
        }

        return self.api_client.call_api(
            '/ingest', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def ingest_post(self, filename : Annotated[constr(strict=True, max_length=100, min_length=1), Field(..., description="Free-form text field to explicitly define the name of the file to be persisted")], body : Union[conbytes(strict=True, min_length=1, max_length=1000000000), constr(strict=True, min_length=1, max_length=1000000000)], notes : Annotated[Optional[constr(strict=True, max_length=10000, min_length=1)], Field(description="Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data)")] = None, type : Annotated[Optional[StrictStr], Field(description="Type of file to be ingested, defaults to 'etuff'")] = None, version : Annotated[Optional[constr(strict=True, max_length=10, min_length=1)], Field(description="Version identifier for the eTUFF tag data file ingested")] = None, **kwargs) -> Ingest200:  # noqa: E501
        """Post a local file and perform a ingest operation  # noqa: E501

        Post a local file and perform a ingest operation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ingest_post(filename, body, notes, type, version, async_req=True)
        >>> result = thread.get()

        :param filename: Free-form text field to explicitly define the name of the file to be persisted (required)
        :type filename: str
        :param body: (required)
        :type body: bytearray
        :param notes: Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data)
        :type notes: str
        :param type: Type of file to be ingested, defaults to 'etuff'
        :type type: str
        :param version: Version identifier for the eTUFF tag data file ingested
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Ingest200
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the ingest_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.ingest_post_with_http_info(filename, body, notes, type, version, **kwargs)  # noqa: E501

    @validate_arguments
    def ingest_post_with_http_info(self, filename : Annotated[constr(strict=True, max_length=100, min_length=1), Field(..., description="Free-form text field to explicitly define the name of the file to be persisted")], body : Union[conbytes(strict=True, min_length=1, max_length=1000000000), constr(strict=True, min_length=1, max_length=1000000000)], notes : Annotated[Optional[constr(strict=True, max_length=10000, min_length=1)], Field(description="Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data)")] = None, type : Annotated[Optional[StrictStr], Field(description="Type of file to be ingested, defaults to 'etuff'")] = None, version : Annotated[Optional[constr(strict=True, max_length=10, min_length=1)], Field(description="Version identifier for the eTUFF tag data file ingested")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Post a local file and perform a ingest operation  # noqa: E501

        Post a local file and perform a ingest operation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ingest_post_with_http_info(filename, body, notes, type, version, async_req=True)
        >>> result = thread.get()

        :param filename: Free-form text field to explicitly define the name of the file to be persisted (required)
        :type filename: str
        :param body: (required)
        :type body: bytearray
        :param notes: Free-form text field where details of submitted eTUFF file for ingest can be provided e.g. submitter name, etuff data contents (tag metadata and measurements + primary position data, or just secondary solution-positional meta/data)
        :type notes: str
        :param type: Type of file to be ingested, defaults to 'etuff'
        :type type: str
        :param version: Version identifier for the eTUFF tag data file ingested
        :type version: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Ingest200, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'filename',
            'body',
            'notes',
            'type',
            'version'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ingest_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('filename') is not None:  # noqa: E501
            _query_params.append(('filename', _params['filename']))

        if _params.get('notes') is not None:  # noqa: E501
            _query_params.append(('notes', _params['notes']))

        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']
            # convert to byte array if the input is a file name (str)
            if isinstance(_body_params, str):
                with io.open(_body_params, "rb") as _fp:
                   _body_params_from_file = _fp.read()
                _body_params = _body_params_from_file

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/octet-stream', 'text/plain']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Ingest200",
            '500': "ErrorContainer",
        }

        return self.api_client.call_api(
            '/ingest', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
