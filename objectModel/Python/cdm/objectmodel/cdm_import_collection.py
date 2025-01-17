﻿# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.

from typing import Optional, Union, TYPE_CHECKING

from cdm.enums import CdmObjectType

from .cdm_collection import CdmCollection, T

if TYPE_CHECKING:
    from .cdm_import import CdmImport


class CdmImportCollection(CdmCollection):
    def __init__(self, ctx: 'CdmCorpusContext', owner: 'CdmObject'):
        super().__init__(ctx, owner, CdmObjectType.IMPORT)

    def append(self, obj: Union[str, 'CdmImport'], moniker: Optional[str] = None) -> 'CdmImport':
        if not isinstance(obj, str):
            return super().append(obj)

        import_value = super().append(obj)
        if moniker is not None:
            import_value.moniker = moniker

        return import_value

    def item(self, corpus_path: str, moniker: Optional[str] = None, check_moniker: Optional[bool] = True) -> 'CdmImport':
        for x in self:
            if check_moniker:
                if x.corpus_path == corpus_path and x.moniker == moniker:
                    return x
            else:
                if x.corpus_path == corpus_path:
                    return x
        return None

