# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import election_pb2 as election__pb2


class ElectionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.resp_serv_id = channel.unary_unary(
                '/Election/resp_serv_id',
                request_serializer=election__pb2.Empty.SerializeToString,
                response_deserializer=election__pb2.response_id.FromString,
                )
        self.resp_permission = channel.unary_unary(
                '/Election/resp_permission',
                request_serializer=election__pb2.request_permission.SerializeToString,
                response_deserializer=election__pb2.response_permission.FromString,
                )
        self.resp_election = channel.unary_unary(
                '/Election/resp_election',
                request_serializer=election__pb2.request_election.SerializeToString,
                response_deserializer=election__pb2.response_election.FromString,
                )
        self.recv_coordinator = channel.unary_unary(
                '/Election/recv_coordinator',
                request_serializer=election__pb2.send_coordinator.SerializeToString,
                response_deserializer=election__pb2.Empty.FromString,
                )


class ElectionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def resp_serv_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def resp_permission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def resp_election(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recv_coordinator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ElectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'resp_serv_id': grpc.unary_unary_rpc_method_handler(
                    servicer.resp_serv_id,
                    request_deserializer=election__pb2.Empty.FromString,
                    response_serializer=election__pb2.response_id.SerializeToString,
            ),
            'resp_permission': grpc.unary_unary_rpc_method_handler(
                    servicer.resp_permission,
                    request_deserializer=election__pb2.request_permission.FromString,
                    response_serializer=election__pb2.response_permission.SerializeToString,
            ),
            'resp_election': grpc.unary_unary_rpc_method_handler(
                    servicer.resp_election,
                    request_deserializer=election__pb2.request_election.FromString,
                    response_serializer=election__pb2.response_election.SerializeToString,
            ),
            'recv_coordinator': grpc.unary_unary_rpc_method_handler(
                    servicer.recv_coordinator,
                    request_deserializer=election__pb2.send_coordinator.FromString,
                    response_serializer=election__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Election', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Election(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def resp_serv_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Election/resp_serv_id',
            election__pb2.Empty.SerializeToString,
            election__pb2.response_id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def resp_permission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Election/resp_permission',
            election__pb2.request_permission.SerializeToString,
            election__pb2.response_permission.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def resp_election(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Election/resp_election',
            election__pb2.request_election.SerializeToString,
            election__pb2.response_election.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def recv_coordinator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Election/recv_coordinator',
            election__pb2.send_coordinator.SerializeToString,
            election__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
